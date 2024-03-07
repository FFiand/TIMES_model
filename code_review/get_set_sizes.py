import pandas as pd
import gamspy as gp
from pathlib import Path

instances = [
    ("1p5C_OS_SSP2", "BASE_SSP2.RUN"),
    ("BAU_IND_V2", "BAU_upd_IND_2050_19a.run"),
    ("BEAM-ME_Instances/672_11_8", "672_11_8.run"),
    ("BEAM-ME_Instances/672_22_8", "672_22_8.run"),
    # ("BEAM-ME_Instances/2016_22_8", "2016_22_8.run"),
    ("E4SMA", "bgm_scen_1p5-r5e.run"),
    ("GAZNAT_V1_Instance", "CLI_CCS_upd_NGFD.RUN"),
    ("Offshore", "offshore.run"),
    ("POLIZERO_V1_Instance", "clipl-2050.run"),
    ("POLIZERO_V2_Instance", "bau-2050_calib.run"),
    ("TIMES-DK-Instance", "SCENARIO.RUN"),
    ("UK-TIMES", "eina_least_cost.run"),
]

df_lst = []

symbols = [
    "Instance",
    "T",
    "TS",
    "TSL",
    "R",
    "S",
    "SL",
    "V",
    "P",
    "C",
    "CG",
    "COM",
    "COM2",
    "COM_VAR",
    "COM_GRP",
    "ALLYEAR",
    "ALL_TS",
    "UC_N",
    "UC_GRPTYPE",
    "BD",
    "L",
    "IO",
    "ITEM",
    "TSLVL",
    "ALLSOW",
]

for i, run_file in instances:
    gdx = Path(f"code_review/output/{i}/ground_truth.gdx")
    c = gp.Container(load_from=gdx)

    lst = []
    for s in symbols:
        if s == "Instance":
            lst.append(i)
        else:
            lst.append(len(c[s].records))

    df_lst.append(lst)

df = pd.DataFrame(df_lst, columns=symbols).set_index("Instance")
df.loc["mean"] = round(df.mean(), 2)
df.loc["median"] = round(df.median(), 2)
df = df.sort_values(axis=1, by="mean")
df.to_string("code_review/set_sizes.txt")

print("done")
