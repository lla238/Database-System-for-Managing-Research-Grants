import sqlite3

def find_open_competitions(month):

    conn = sqlite3.connect('council.db')
    cursor = conn.cursor()

    
    cursor.execute("""
        SELECT DISTINCT gc.competition_id, gc.title
        FROM GrantCompetition gc
        JOIN GrantProposal gp ON gc.competition_id = gp.competition_id
        WHERE strftime('%m', gc.application_deadline) = ?
          AND gc.status = 'open'
          AND gp.status IN ('submitted', 'awarded', 'not awarded')
          AND (gp.amount_requested > 20000 OR
               (SELECT COUNT(*)
                FROM Researcher r
                WHERE r.researcher_id = gp.principal_investigator_id) > 10)
    """, (month,))


    competitions = cursor.fetchall()


    conn.close()

    return competitions

def main():

    month = input("Enter a month (MM): ")

    
    competitions = find_open_competitions(month)

    
    if competitions:
        print("Competitions open in month {} with at least one submitted large proposal:".format(month))
        for competition in competitions:
            print("Competition ID:", competition[0])
            print("Title:", competition[1])
            print()
    else:
        print("No competitions found for the specified month.")

if __name__ == "__main__":
    main()


def find_largest_amount_proposals(area):
    
    conn = sqlite3.connect('council.db')
    cursor = conn.cursor()

    
    sql_query = """
                SELECT proposal_id, amount_requested
                FROM GrantProposal
                WHERE competition_id IN (
                    SELECT competition_id
                    FROM GrantCompetition
                    WHERE area = ?
                )
                ORDER BY amount_requested DESC
                LIMIT 1
                """

   
    cursor.execute(sql_query, (area,))
    result = cursor.fetchone()


    conn.close()

    
    if result:
        proposal_id, amount_requested = result
        print(f"The proposal with the largest amount of money requested for area '{area}' is:")
        print(f"Proposal ID: {proposal_id}, Amount Requested: {amount_requested}")
    else:
        print(f"No proposal found for area '{area}'")


area_input = input("Enter the area to find the largest amount proposals: ")
find_largest_amount_proposals(area_input)



def find_proposals_awarded_before_date(date):
 
    conn = sqlite3.connect('council.db')
    cursor = conn.cursor()

    
    sql_query = """
                SELECT proposal_id, amount_awarded
                FROM GrantProposal
                WHERE status = 'awarded'
                    AND date_awarded <= ?
                ORDER BY amount_awarded DESC
                LIMIT 1
                """


    cursor.execute(sql_query, (date,))
    result = cursor.fetchone()

 
    conn.close()

  
    if result:
        proposal_id, amount_awarded = result
        print(f"The proposal submitted before {date} that is awarded the largest amount of money is:")
        print(f"Proposal ID: {proposal_id}, Amount Awarded: {amount_awarded}")
    else:
        print(f"No awarded proposal found submitted before {date}")


date_input = input("Enter the date (YYYY-MM-DD) to find awarded proposals submitted before that date: ")
find_proposals_awarded_before_date(date_input)



def calculate_average_discrepancy(area):
 
    conn = sqlite3.connect('council.db')
    cursor = conn.cursor()

 
    sql_query = """
                SELECT AVG(ABS(amount_requested - amount_awarded)) AS avg_discrepancy
                FROM GrantProposal
                JOIN GrantCompetition ON GrantProposal.competition_id = GrantCompetition.competition_id
                WHERE GrantCompetition.area = ?
                """

   
    cursor.execute(sql_query, (area,))
    result = cursor.fetchone()

 
    conn.close()

   
    if result[0]:
        avg_discrepancy = result[0]
        print(f"The average requested/awarded discrepancy for the area '{area}' is: {avg_discrepancy}")
    else:
        print(f"No proposals found for the area '{area}'")


area_input = input("Enter the area to calculate the average requested/awarded discrepancy: ")
calculate_average_discrepancy(area_input)





