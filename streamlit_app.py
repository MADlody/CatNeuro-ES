import streamlit as st

def main():
    # --- Page Configuration ---
    st.set_page_config(
        page_title="Cat Neurological Diagnosis Expert System",
        page_icon="🐱",
        layout="wide"
    )

    # --- Header & Project Details ---
    st.title("🐱 Cat Neurological Diagnosis Expert System")
    st.markdown("""
    **Course:** Knowledge-Based Systems (ISP543)  
    **Faculty:** Faculty of Computer Science and Mathematics, UiTM  
    **Prepared For:** Dr. Mohd Zaki B Zakaria
    """)

    with st.expander("View Group Members"):
        st.write("""
        * **Mohamad Harith Nazrin Bin Mohd Nazri** (2025112205)
        * **Meor Afif Dinie Bin Meor Muhammad Azmi** (2025119705)
        * **Muhammad Afiq Afief Bin Nor Haizan** (2025145015)
        * **Muhammad Azry Hakimi Bin Khezri Kamil** (2025118351)
        * **Afif Haikal Bin Amin Farhan** (2025160587)
        * **Jibran Naqib Bin Saiful Bakhri** (2025133461)
        """)

    st.markdown("---")

    # --- Sidebar Inputs (1.0 INPUT) ---
    st.sidebar.header("1.0 Input Symptoms")

    # Mapping inputs exactly as per the PDF documentation
    weakness = st.sidebar.selectbox(
        "General Weakness",
        options=["None", "Mild", "Severe"],
        index=0
    )

    balance_problems = st.sidebar.radio(
        "Balance Problems (Ataxia)",
        options=["Yes", "No"],
        index=1
    )

    seizures = st.sidebar.selectbox(
        "Seizures",
        options=["None", "Rare", "Frequent"],
        index=0
    )

    behavior_changes = st.sidebar.selectbox(
        "Behavioral Changes",
        options=["None", "Mild", "Major"],
        index=0
    )

    incontinence = st.sidebar.radio(
        "Incontinence (Bowel Control Issues)",
        options=["Yes", "No"],
        index=1
    )

    head_neck_weakness = st.sidebar.radio(
        "Head or Neck Weakness",
        options=["Yes", "No"],
        index=1
    )

    age_group = st.sidebar.selectbox(
        "Age Group",
        options=["Kitten", "Adult", "Senior"],
        index=1
    )

    recent_trauma = st.sidebar.radio(
        "Recent Trauma or Infections",
        options=["Yes", "No"],
        index=1
    )

    # --- Logic Evaluation (3.0 RULES) ---
    # We collect all triggered rules into a list
    diagnoses = []

    # Rule 1
    # IF balance_problems = yes AND behavior_changes = none
    # THEN output = "Possible Vestibular Syndrome"
    if balance_problems == "Yes" and behavior_changes == "None":
        diagnoses.append("Possible Vestibular Syndrome")

    # Rule 2
    # IF seizures = rare AND behavior_changes != major
    # THEN output = "Possible Mild Seizure Disorder"
    if seizures == "Rare" and behavior_changes != "Major":
        diagnoses.append("Possible Mild Seizure Disorder")

    # Rule 3
    # IF seizures = frequent
    # THEN output = "Possible Severe Seizure Disorder / Epilepsy"
    if seizures == "Frequent":
        diagnoses.append("Possible Severe Seizure Disorder / Epilepsy")

    # Rule 4
    # IF age_group = senior AND seizures != none AND behavior_changes = major
    # THEN output = "Possible Brain Tumor or Age-Related Brain Disease"
    if age_group == "Senior" and seizures != "None" and behavior_changes == "Major":
        diagnoses.append("Possible Brain Tumor or Age-Related Brain Disease")

    # Rule 5
    # IF age_group = senior AND (behavior_changes = mild OR behavior_changes = major) AND seizures = none
    # THEN output = "Possible Cognitive Dysfunction (Senior Dementia)"
    if age_group == "Senior" and (behavior_changes == "Mild" or behavior_changes == "Major") and seizures == "None":
        diagnoses.append("Possible Cognitive Dysfunction (Senior Dementia)")

    # Rule 6
    # IF balance_problems = yes AND incontinence = yes
    # THEN output = "Possible Spinal Cord Disorder"
    if balance_problems == "Yes" and incontinence == "Yes":
        diagnoses.append("Possible Spinal Cord Disorder")

    # Rule 7
    # IF head_neck_weakness = yes AND weakness = severe
    # THEN output = "Possible Neuromuscular Disorder"
    if head_neck_weakness == "Yes" and weakness == "Severe":
        diagnoses.append("Possible Neuromuscular Disorder")

    # Rule 8
    # IF age_group = kitten AND balance_problems = yes
    # THEN output = "Possible Congenital Neurological Disorder"
    if age_group == "Kitten" and balance_problems == "Yes":
        diagnoses.append("Possible Congenital Neurological Disorder")

    # Rule 9
    # IF trauma_or_infection = yes AND seizures != none
    # THEN output = "Possible Infection / Toxin / Inflammatory Neurological Condition"
    if recent_trauma == "Yes" and seizures != "None":
        diagnoses.append("Possible Infection / Toxin / Inflammatory Neurological Condition")

    # --- Output Display (2.0 OUTPUT) ---
    st.subheader("Diagnosis Results")

    if st.button("Run Diagnosis", type="primary"):
        if diagnoses:
            st.success("The Expert System has identified the following potential issues:")
            for i, diagnosis in enumerate(diagnoses, 1):
                st.write(f"**{i}. {diagnosis}**")
        else:
            st.info("No specific diagnosis matched the current rules based on your inputs.")
            st.markdown("*Try adjusting the symptoms in the sidebar if you suspect a specific condition.*")
    else:
        st.write("Adjust the symptoms in the sidebar and click **Run Diagnosis**.")

if __name__ == "__main__":
    main()
