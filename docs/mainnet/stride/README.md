# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/stride.png" width="150" alt=""><figcaption></figcaption></figure>

Stride is a blockchain ("zone") that provides liquidity for staked assets.  Using Stride, you can earn both staking and DeFi yields across the Cosmos IBC ecosystem

**Chain ID**: stride-1 | **Latest Version Tag**: v4.0.2 | **Wasm**: OFF

[Website](https://stride.zone) | [Discord](https://discord.gg/mzQZ8dAE7u) | [Twitter](https://twitter.com/stride_zone)

## Restake

[Restake with kjnodes](https://restake.app/stride/stridevaloper1j8gkhtllnp252l6g6zwzea30e7pvzqttr9768n) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://stride.rpc.kjnodes.com](https://stride.rpc.kjnodes.com)
* api: [https://stride.api.kjnodes.com](https://stride.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stride.rpc.kjnodes.com:16656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stride.rpc.kjnodes.com:16659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/stride/addrbook.json > $HOME/.stride/config/addrbook.json
```

**live-peers** (40)
```
peers="0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.187:26656,7ee622727088106f07402fa1e9004fdb2d504bf6@176.9.188.21:51656,d77e7918b9f9e21ee60a8e03075ca3e5f7353912@162.55.4.253:26656,f420eab70caad310ad6cc1990c977cadf193264c@51.159.80.121:6000,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,93d7b9da65d31e052027abf20fab35ff31d3d826@195.20.240.90:26656,e37c0178e07c5de335c0e6293fec39b473e7f1e1@65.109.52.178:26656,157000d06040f2a7b981c6f062da0c9da0e6e6af@194.163.163.0:26656,4d17c6e85a1e6282efee950ff3dfe85b4b043f0f@148.251.51.144:26656,950da031d9536b9fbd0e9f0c70d65740d11d0111@192.118.76.122:26656,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,df3f533e6b9776c11f08da804edcb810cbdd2080@65.108.234.23:12256,28db7a664e95241930c5680ad2e1480bed3fb99f@198.244.178.213:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,a757fc9ea95a7f643d392ec9fdaa31cbf06e76d9@195.3.221.21:12256,0e202ae079fb8b1849993ef6e6e6bd012b10374f@46.4.81.204:45656,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,777274fb08ed48a4e027664e2576a8460272e43c@15.235.115.153:26656,b6bbf3fce8563bf55cee37776d1cfc3e6692c7e6@167.235.1.101:26656,471518432477e31ea348af246c0b54095d41352c@78.47.210.211:26656,d13d51e660dbd89d6660ac9b61957c5e727efdae@135.181.130.145:6000,87ba7609ae2aae4c048ef83687fc913b8866cc0b@194.163.161.146:16656,8fff37214fb0ef622f1c09dccb22d6321e004c3e@109.123.242.163:50056,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,8d7d0f32d53467c4d5e8871faf4ec58ea970fed2@157.90.179.182:26456,6b615c7dde3e76de39474b7406bdde0ac0f31b79@23.88.69.22:28666,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,6a6a70719d44dfdaa74a074f017dc1f1ff23da62@146.59.0.123:6000,8ade90b45b991088c92e8583e8bc93589d6cd81e@84.244.95.247:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,20948180a8b777f9bbfae3c4bdcc340a04dffdc0@89.58.57.39:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,a3f95b0b15c31a68a7535f6068c4e14b95e90dcf@65.109.92.240:21016,cfd27429d382ecf366ddad02c88f15a8753092c8@66.172.36.135:28656,2c1f55e905c7425f995947e2d600ca5ac863b8c1@15.235.53.91:13456,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,6856de6f0c70a850db2b58deb43d568fced4a524@35.208.90.201:26656,f5732d5a406bdbbf08acad017c0993c0aa8ebe70@34.145.16.183:26656,98ea86b6dd2786820ec7f9f2b697d7083de43135@38.146.3.120:12256"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
