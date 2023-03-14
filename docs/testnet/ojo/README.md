# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" width="150" alt=""><figcaption></figcaption></figure>

Ojo is a decentralized security-first oracle network built  to support the Cosmos Ecosystem. Ojo will source price data  from a diverse catalog of on and off-chain sources and use  advanced security mechanisms to guarantee the integrity of the data it provides.

**Chain ID**: ojo-devnet | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://ojo.network) | [Discord](https://discord.gg/fd8Yrex8nC) | [Twitter](https://twitter.com/ojo_network)




## Chain explorer
[https://explorer.kjnodes.com/ojo-testnet](https://explorer.kjnodes.com/ojo-testnet)

## Public endpoints

* api: [https://ojo-testnet.api.kjnodes.com](https://ojo-testnet.api.kjnodes.com)
* rpc: [https://ojo-testnet.rpc.kjnodes.com](https://ojo-testnet.rpc.kjnodes.com)
* grpc: [https://ojo-testnet.grpc.kjnodes.com](https://ojo-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ojo-testnet.rpc.kjnodes.com:50656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ojo-testnet.rpc.kjnodes.com:50659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ojo-testnet/addrbook.json > $HOME/.ojo/config/addrbook.json
```

**live-peers** (40)
```bash
peers="e6630a82c1c5cc42e904e74dd2e0de6dd5113efe@148.251.90.138:18656,2c40b0aedc41b7c1b20c7c243dd5edd698428c41@138.201.85.176:26696,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,b0968b57bcb5e527230ef3cfa3f65d5f1e4647dd@35.212.224.95:26656,bdd24cab3246503ae261aea82f077ffb66d56ce3@95.216.39.183:28656,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,d5b2ae8815b09a30ab253957f7eca052dde3101d@65.108.9.164:24656,ea0ad608f0fa47e20047569c7c0c1ff76dd3d724@45.151.123.72:28656,8b6c75d20ac3ceeb7f0f1d4b5fc89a69e567c47b@65.108.231.238:36656,bf834f428aed19dd1937d66327cb6244d7722b0d@65.108.201.189:26676,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,a9bcb95ee047c4a909c675dc36c556eafe1248e1@195.201.174.109:46656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,c2ed1269cd275202e4d69fdb64e194e59b20f573@185.245.182.152:40656,ed12aee3273baaaf01e357574c1692f12776446d@65.109.117.165:50656,783187fd50077da7a373ad020a37d47f2d87cd9b@164.90.220.252:32656,4609153f2b095b6c7f98b9cd3d079fe8fcd992db@95.216.14.58:61356,4764a447ea3518e5017756b42ca5f6442b2f5768@5.161.114.1:26656,91eba8f362b6c41d324ff26f316ce0b50d22b955@213.136.84.176:10656,969b1e53d217abf769054777190f9a65eb8174cf@46.4.61.91:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,863a266ca1a958b9d122511289041905120e26dd@185.245.183.254:26656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,a16f9bf520996da6df0939bb5f0a510fa1f59420@168.138.197.232:28656,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,fb45d68ce227d2bd3b112d26d27341faebc3736e@78.46.61.117:03656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,9015c79a2ae5a0033f4ee9237a19ea67579e37f8@135.181.57.104:26656,d69bb338dcc2aa6a00961731b4ca6746132ef356@1.162.37.101:26656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,50e9bd8647571268df2313df6c46ba9960c9f40e@178.128.88.30:26656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:26656,a3a9014f82cb69fe0494ea3bc49990027d081a5a@65.108.126.35:36656,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:21656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
