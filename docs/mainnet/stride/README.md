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

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@stride.rpc.kjnodes.com:16656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@stride.rpc.kjnodes.com:16659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/stride/addrbook.json > $HOME/.stride/config/addrbook.json
```

**live-peers** (35)
```bash
peers="741864e5c0bd37ae602c2c853c71a2c3b84589a0@65.21.88.172:29656,ed857708c330334e1e62751470d6ecddf0397459@65.109.69.59:12256,a83cd29f4f9a4711346184966f9fb6c80bb658d2@65.108.103.184:21656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.155:26656,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,261e8dfcf7fddb5b62c48eea3b7fdd11335ae21f@185.119.118.117:2000,4d17c6e85a1e6282efee950ff3dfe85b4b043f0f@148.251.51.144:26656,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,28db7a664e95241930c5680ad2e1480bed3fb99f@198.244.178.213:26656,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,b6bbf3fce8563bf55cee37776d1cfc3e6692c7e6@167.235.1.101:26656,ef22ceb48d8d7548fab0972a5e4a9cb3c366fc74@65.109.52.178:26656,f1329fdfcc5ec83ee4f52c71a3b5b611006bee1d@149.202.72.186:26639,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,dedfec7d7356da68baaaa7841b66b5fcc594767e@65.109.37.154:2000,87ba7609ae2aae4c048ef83687fc913b8866cc0b@194.163.161.146:16656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,6856de6f0c70a850db2b58deb43d568fced4a524@35.208.90.201:26656,01899588499352857c214c50451c5fa59744ace2@88.99.161.228:26656,a7b4cf6f65138ba61518c2c45402da32dc8e28b7@88.99.164.158:21016,a757fc9ea95a7f643d392ec9fdaa31cbf06e76d9@195.3.221.21:12256,be0522cbc5ea30f14355ff6d05ed4b9cf47d7dda@188.172.228.162:26656,d77e7918b9f9e21ee60a8e03075ca3e5f7353912@162.55.4.253:26656,5b20fde898024d705cba65ba9a9352f8a4a2d8d2@142.132.244.107:27012,90fbbe59cf9c6371b2557ab8f4ff1389f83c2c81@51.81.57.144:26656,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,157000d06040f2a7b981c6f062da0c9da0e6e6af@194.163.163.0:26656,a2128f5552cf4ae60a769999c7fddc5d9d44d149@15.235.42.151:26661,a3f95b0b15c31a68a7535f6068c4e14b95e90dcf@65.109.92.240:21016,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,c484f998e1a9e464a68af04d8d15d6fb0aeceb1e@65.21.129.95:26656,bbe196ec7c537e9dac0d2575350a1aa64700cdef@129.213.159.218:26656,98ea86b6dd2786820ec7f9f2b697d7083de43135@38.146.3.120:12256,8fff37214fb0ef622f1c09dccb22d6321e004c3e@109.123.242.163:50056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
