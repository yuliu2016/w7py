import pandas
import tbapy

schedule = pandas.DataFrame((lambda x: [{"{} {}".format(a.capitalize(), b + 1):
                                        int(x[mn]["alliances"][a]["team_keys"][b][3:])
                                         for a in ["red", "blue"] for b in [0, 1, 2]}
                                        for mn in sorted(x.keys())])
                            ({match["match_number"]: match for match in
                              tbapy.TBA(
                                  "luXn9AfDrhfEJHZ1zOPHyDdxv4XY7Iqt71NuvhRfa0EKfPBGLyyai8DFAuyjrEAt").
                             event_matches("2018dar", simple=True)
                              if match["comp_level"] == "qm"}),
                            columns=["{} {}".format(a, b)
                                     for a in ["Red", "Blue"] for b in [1, 2, 3]])
schedule.index += 1
print(schedule)
