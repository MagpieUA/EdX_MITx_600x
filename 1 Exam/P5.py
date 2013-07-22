def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story. 
    """
    words = story.split()
    result = ""
    for word in words:
        if word in listOfAdjs:
            result = result + '[ADJ]' + ' '
        elif word in listOfNouns:
            result = result + '[NOUN]' + ' '
        elif word in listOfVerbs:
            result = result + '[VERB]' + ' '
        else:
            result = result + word + ' '
    result = result [:-1]
    return result

def generateTemplates(madLibsForm):
    """ 
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.
    """
    words = madLibsForm.split()
    template = ['[ADJ]', '[NOUN]', '[VERB]']
    result = []
    for word in words:
        if word in template:
            result.append(word)
    return result

def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    if madTemplate == '[ADJ]':
        return userWord in listOfAdjs
    elif madTemplate == '[NOUN]':
        return userWord in listOfNouns
    elif madTemplate == '[VERB]':
        return userWord in listOfVerbs

story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
listOfAdjs = ['creepy', 'plaid']
listOfNouns = ['store', 'pants', 'something', 'grandpa']
listOfVerbs = ['found', 'looked']
madlibsform = generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
print madlibsform
template = generateTemplates(madlibsform)
print template

