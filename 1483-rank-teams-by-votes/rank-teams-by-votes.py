class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        team_map = {team: [0]*n for team in votes[0]}

        for vote in votes:
            for position,team in enumerate(vote):
                team_map[team][position] += 1

        teams = list(votes[0])

        teams.sort(key = lambda team:(*[-x for x in team_map[team]],team))

        return "".join(teams)
        