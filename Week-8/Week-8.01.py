Given an array of names of candidates in an election. A candidate name in the array represents a vote cast to the candidate. Print the name of candidates received Max vote. If there is tie, print a lexicographically smaller name.

Examples: 

Input :  votes[] = {"john", "johnny", "jackie",

                    "johnny", "john", "jackie",

                    "jamie", "jamie", "john",

                    "johnny", "jamie", "johnny",

                    "john"};

Output : John

We have four Candidates with name as 'John', 'Johnny', 'jamie', 'jackie'. The candidates John and Johny get maximum votes. Since John is alphabetically smaller, we print it. Use dictionary to solve the above problem

 

Sample Input:

10

John

John

Johny

Jamie

Jamie

Johny

Jack

Johny

Johny

Jackie

 

Sample Output:

Johny

 

 

 










def find_winner(votes):
    vote_count = {}
    for name in votes:
        if name in vote_count:
            vote_count[name] += 1
        else:
            vote_count[name] = 1
    
    max_votes = max(vote_count.values())
    winners = [name for name, votes in vote_count.items() if votes == max_votes]
    winner = sorted(winners)[0]
    
    return winner

n = int(input())
votes = [input() for _ in range(n)]
winner = find_winner(votes)
print(winner)
