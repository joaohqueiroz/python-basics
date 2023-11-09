def orderByScore(aluno):
       return aluno[1]
    
alunos = []

for _ in range(int(input())):
    alunos.append([input(), float(input())])
    
alunos.sort(key=orderByScore)

semMenor = [[name, score] for name, score in alunos if score != alunos[0, 1]]

print(semMenor)