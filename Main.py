#Team formation tool
Here's the updated code with output:


```
class TeamFormationTool:
    def __init__(self):
        self.team_members = {}
        self.teams = {}

    def add_member(self, name, skill_set):
        """Add a team member with their skill set."""
        self.team_members[name] = skill_set

    def form_teams(self, team_size):
        """Form teams of specified size."""
        members = list(self.team_members.items())
        self.teams = {}
        team_count = 1

        for i in range(0, len(members), team_size):
            team_name = f"Team {team_count}"
            self.teams[team_name] = members[i:i + team_size]
            team_count += 1

    def display_teams(self):
        """Display formed teams."""
        for team_name, members in self.teams.items():
            print(f"\n{team_name}:")
            for member, skills in members:
                print(f"{member} - {', '.join(skills)}")


def main():
    tool = TeamFormationTool()

    while True:
        print("\nTeam Formation Tool")
        print("1. Add Team Member")
        print("2. Form Teams")
        print("3. Display Teams")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter member name: ")
            skill_set = input("Enter skill set (comma-separated): ").split(',')
            skill_set = [skill.strip() for skill in skill_set]
            tool.add_member(name, skill_set)
            print(f"Member {name} added successfully.")
        elif choice == "2":
            team_size = int(input("Enter team size: "))
            tool.form_teams(team_size)
            print(f"Teams formed successfully with {team_size} members each.")
        elif choice == "3":
            tool.display_teams()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
``'


**Output:**

```
Team Formation Tool
1. Add Team Member
2. Form Teams
3. Display Teams
4. Exit
Choose an option: 1
Enter member name: John Doe
Enter skill set (comma-separated): Python, Java, C++
Member John Doe added successfully.


Team Formation Tool
1. Add Team Member
2. Form Teams
3. Display Teams
4. Exit
Choose an option: 1
Enter member name: Jane Doe
Enter skill set (comma-separated): JavaScript, HTML, CSS
Member Jane Doe added successfully.


Team Formation Tool
1. Add Team Member
2. Form Teams
3. Display Teams
4. Exit
Choose an option: 1
Enter member name: Bob Smith
Enter skill set (comma-separated): C#, Ruby, PHP
Member Bob Smith added successfully.


Team Formation Tool
1. Add Team Member
2. Form Teams
3. Display Teams
4. Exit
Choose an option: 2
Enter team size: 2
Teams formed successfully with 2 members each.


Team Formation Tool
1. Add Team Member
2. Form Teams
3. Display Teams
4. Exit
Choose an option: 3


Team 1:
John Doe - Python, Java, C++
Jane Doe - JavaScript, HTML, CSS


Team 2:
Bob Smith - C#, Ruby, PHP


Team Formation Tool
1. Add Team Member
2. Form Teams
3. Display Teams
4. Exit
Choose an option: 4
Exiting the program.
```
```
