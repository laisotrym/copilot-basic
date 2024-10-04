// src/hooks/useForm.js
import { useState } from 'react';

const useCreateUser = (initialState, validate) => {
    const [formData, setFormData] = useState(initialState);
    const [errors, setErrors] = useState({});

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleValidation = () => {
        const newErrors = validate(formData);
        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    return {
        formData,
        errors,
        handleChange,
        handleValidation
    };
};

export default useForm;