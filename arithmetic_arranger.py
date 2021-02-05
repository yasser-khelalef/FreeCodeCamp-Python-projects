def arithmetic_arranger(problems, answer =False):
  if len(problems)>5:
    return "Error: Too many problems."
  else:
    problems_list_of_dicts=list()
    for problem in problems:
      dict_of_problem=dict()
      problem_list = problem.split(' ')
      if len(problem_list[0])<5 and len(problem_list[2])<5:
        try:
          dict_of_problem["num1_length"]=len(problem_list[0])
          dict_of_problem["num2_length"]=len(problem_list[2])
          if len(problem_list[0])>=len(problem_list[2]):
            dict_of_problem['maxspace']=len(problem_list[0])+2
          else:
            dict_of_problem['maxspace']=len(problem_list[2])+2
          dict_of_problem['num1']=int(problem_list[0])
          dict_of_problem['num2']=int(problem_list[2])
        except:
          return "Error: Numbers must only contain digits."
      else:
        return "Error: Numbers cannot be more than four digits"
      
      if problem_list[1]== "+" or problem_list[1]=="-":
        dict_of_problem['oper'] = problem_list[1]
      else:
        return "Error: Operator must be '+' or '-'."
      problems_list_of_dicts.append(dict_of_problem)
    
    for problem_dict in problems_list_of_dicts:
      if problem_dict['oper']=="+":
        problem_dict['result']= problem_dict['num1']+problem_dict['num2']
        problem_dict["result_length"] = len(str(problem_dict['result']))
      elif problem_dict['oper']=="-":
        problem_dict['result']= problem_dict['num1']-problem_dict['num2']
        problem_dict["result_length"] = len(str(problem_dict['result']))
    
    spaces={
      1:" ",
      2:"  ",
      3:"   ",
      4:"    ",
      5:"     "
    }
    firstline=""
    last_item = problems_list_of_dicts[len(problems_list_of_dicts)-1]
    for problem_dict in problems_list_of_dicts:
        if problem_dict != last_item:
            firstline = firstline + spaces[problem_dict["maxspace"]-problem_dict["num1_length"]] + str(problem_dict["num1"]) + spaces[4]
        else:
            firstline = firstline + spaces[problem_dict["maxspace"]-problem_dict["num1_length"]] + str(problem_dict["num1"])

    secondline=""
    for problem_dict in problems_list_of_dicts:
        if problem_dict != last_item:
            secondline= secondline + problem_dict["oper"] + spaces[problem_dict["maxspace"]-problem_dict["num2_length"]-1] + str(problem_dict["num2"])+ spaces[4]
        else:
            secondline= secondline + problem_dict["oper"] + spaces[problem_dict["maxspace"]-problem_dict["num2_length"]-1] + str(problem_dict["num2"])

    thirdline=""
    for problem_dict in problems_list_of_dicts:
      dashes=""
      for i in range(problem_dict["maxspace"]):
        dashes = dashes +"-"
      if problem_dict != last_item:
        thirdline= thirdline + dashes + spaces[4]
      else:
        thirdline= thirdline + dashes
       
    fourthline=""
    for problem_dict in problems_list_of_dicts:
        if problem_dict != last_item:
            fourthline = fourthline + spaces[problem_dict["maxspace"]- problem_dict['result_length']]+str(problem_dict["result"])+spaces[4]
        else:
            fourthline = fourthline + spaces[problem_dict["maxspace"]- problem_dict['result_length']]+str(problem_dict["result"])

    
      
    if answer == True:
        result= firstline+"\n"+secondline+"\n"+thirdline+"\n"+fourthline
    else:
        result= firstline+"\n"+secondline+"\n"+thirdline
    return result





a =arithmetic_arranger(["3 + 855", "3501 - 2", "45 + 43", "123 + 49"], True)
print(a)

