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

**live-peers** (41)
```
peers="cfd27429d382ecf366ddad02c88f15a8753092c8@66.172.36.135:28656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,b212d5740b2e11e54f56b072dc13b6134650cfb5@164.152.160.97:26656,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,b6bbf3fce8563bf55cee37776d1cfc3e6692c7e6@167.235.1.101:26656,d77e7918b9f9e21ee60a8e03075ca3e5f7353912@162.55.4.253:26656,4d17c6e85a1e6282efee950ff3dfe85b4b043f0f@148.251.51.144:26656,950da031d9536b9fbd0e9f0c70d65740d11d0111@192.118.76.122:26656,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,f420eab70caad310ad6cc1990c977cadf193264c@51.159.80.121:6000,6856de6f0c70a850db2b58deb43d568fced4a524@35.208.90.201:26656,28db7a664e95241930c5680ad2e1480bed3fb99f@198.244.178.213:26656,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,e37c0178e07c5de335c0e6293fec39b473e7f1e1@65.109.52.178:26656,a757fc9ea95a7f643d392ec9fdaa31cbf06e76d9@195.3.221.21:12256,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.44.213:26656,698ecde23465c1d01d02cc364f36426d259ba1f0@192.99.247.170:26656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.155:26656,df7ea6950a4a58199ba03ba9454ded0d51f38003@188.217.162.92:26656,f5732d5a406bdbbf08acad017c0993c0aa8ebe70@34.145.16.183:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,7ee622727088106f07402fa1e9004fdb2d504bf6@176.9.188.21:51656,8d7d0f32d53467c4d5e8871faf4ec58ea970fed2@157.90.179.182:26456,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,6a6a70719d44dfdaa74a074f017dc1f1ff23da62@146.59.0.123:6000,d13d51e660dbd89d6660ac9b61957c5e727efdae@135.181.130.145:6000,bde0ccb7d858f2e5ab8c12cd78bf360c6614535f@142.132.199.211:26653,df3f533e6b9776c11f08da804edcb810cbdd2080@65.108.234.23:12256,90fbbe59cf9c6371b2557ab8f4ff1389f83c2c81@51.81.57.144:26656,5285512b3ef0979823d43b4bdc393db31f11a84d@34.170.17.239:26656,c6d54f5554078d513a3cabc9106798837561ca6b@65.144.145.234:26656,6b615c7dde3e76de39474b7406bdde0ac0f31b79@23.88.69.22:28666,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,06c309d890fe6a1e7d2ac0a600ab077d1e793e18@51.195.89.43:10156,8fff37214fb0ef622f1c09dccb22d6321e004c3e@109.123.242.163:50056,20948180a8b777f9bbfae3c4bdcc340a04dffdc0@89.58.57.39:26656,e821acdaf0c7a3c60ea3cd4eb4a98a62dad06f58@43.201.12.41:26656,87ba7609ae2aae4c048ef83687fc913b8866cc0b@194.163.161.146:16656,dc9241e56b67b2d9b39a79f4aa9dc432d78c1dbc@195.3.223.204:10156,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@135.181.5.219:12256"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
