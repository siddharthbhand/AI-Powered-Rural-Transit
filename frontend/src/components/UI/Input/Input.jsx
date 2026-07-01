import styles from "./Input.module.css";

function Input({
  label,
  type = "text",
  placeholder,
  value,
  onChange,
}) {
  return (
    <div className={styles.inputGroup}>
      {label && <label className={styles.label}>{label}</label>}

      <input
        className={styles.input}
        type={type}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
      />
    </div>
  );
}

export default Input;