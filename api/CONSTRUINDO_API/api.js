const apiUrl = 'https://jsonplaceholder.typicode.com/users/3';

async function fetchUsers() {
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error("Erro ao recuperar usuários");
        }
        const users = await (response.json());

        console.log("Usuários", users);



    } catch (error) {
        console.error("Erro:", error);
    }
}

fetchUsers();