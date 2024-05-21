# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\2. Series At A Glance
'''
                            Selection By Label

Approach                        Example                     Comment
[]indexing                      series['label']             slices, callables, boolean masks
.loc[]                          series.loc['label']         slices, callables, boolean masks
dot access                      series.label                no slice or boolean mask support
.get()                          series.get                  no slice support provides default forgiving

                            Selection By Position
[]indexing                      series[0]                   slices, callables, boolean masks
.iloc[]                         series.iloc[0]              slices, callables, boolean masks
X dot access                    series.0                    no slice or boolean mask support
.get()                          series.get(0)               no slice support, provides default, forgiving
'''