from js import document
import json  
from pyodide.ffi import create_proxy

#yes organizers this email testCase is AI generated, this will not be used in the final examination
testCase = """Dear Valued Customer,

We detected unusual sign-in activity on your account from an
unrecognized device. For your protection, your account has been limited.

Your account will be suspended within 24 hours unless you verify your
identity immediately.

Click here to verify your account: http://acmebank-verify.example.com/login

You will need to enter your password and the one-time code we send to
your phone. Failure to respond will result in permanent closure of your
account.

Please do not discuss this notice with anyone, including bank staff,
as this may delay the process.

Thank you for your cooperation,
Acme Bank Security Department"""

def phraseSeparater(raw_email: str) -> list:
  #print(raw_email)
  lowc_email = raw_email.lower()
  #print(lowc_email)

  phrases = []
  
  lines = (lowc_email.strip().split("."))
  #print(lines)
  for line in lines:
    if len(line.split()) == 1:
      continue
    
    cur_Line = ""
    for i, char in enumerate(line):
      if char == "\n":
        cur_Line = f"{line[:i]} {line[(i+1):]}"
      else:
        cur_Line = line

      
    
    phrases.append(cur_Line)

  phrases = [p for p in phrases if p]
  
  return phrases
  
  
def scoreTotalCalculation(phrases: list) -> int:
  #def algo logic
  total = len(phrases)*4
  
  return total

def scamScoreEvaluator(raw_email: str) -> int:
  pass
  
  
def scamEvaluate(event):
    name = document.getElementById("name").value
    print(phraseSeparater(name))
    document.getElementById("output").innerText = f"Hello, {name}!"
  

#print(phraseSeparater(testCase))
document.getElementById("hello").addEventListener("click", create_proxy(scamEvaluate))

