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

**live-peers** (34)
```
peers="f420eab70caad310ad6cc1990c977cadf193264c@51.159.80.121:6000,d77e7918b9f9e21ee60a8e03075ca3e5f7353912@162.55.4.253:26656,4d17c6e85a1e6282efee950ff3dfe85b4b043f0f@148.251.51.144:26656,950da031d9536b9fbd0e9f0c70d65740d11d0111@192.118.76.199:26626,6856de6f0c70a850db2b58deb43d568fced4a524@35.208.90.201:26656,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,ef22ceb48d8d7548fab0972a5e4a9cb3c366fc74@65.109.52.178:26656,28db7a664e95241930c5680ad2e1480bed3fb99f@198.244.178.213:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,cc21cd5beebca219107c3cb31a01c21adb76670b@34.79.153.13:26656,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,01899588499352857c214c50451c5fa59744ace2@88.99.161.228:26656,b6bbf3fce8563bf55cee37776d1cfc3e6692c7e6@167.235.1.101:26656,8d7d0f32d53467c4d5e8871faf4ec58ea970fed2@157.90.179.182:26456,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,ed857708c330334e1e62751470d6ecddf0397459@65.109.69.59:12256,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,bf9168fbcc7250c7c5b9d8080cd4eeee6e399913@95.214.53.214:26886,18704d8ffb35d412adb3fb8eea62c894cf175e75@86.48.26.130:26656,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,a757fc9ea95a7f643d392ec9fdaa31cbf06e76d9@195.3.221.21:12256,5e0250a806113d60be48fab434ed81bb3e41be13@192.99.14.194:26656,82588f011491c6100d922d133f52fc23460b9231@135.181.67.235:26656,4040b0b8a983a8073319163c5ab67cb1b0a19d36@185.245.182.112:26656,1387946c04bceb472113f657f55f670f71709230@65.108.4.188:12256,a4b4e2befe485ab1bc4d05775162d1edbaad428a@137.184.9.18:31309,a3f95b0b15c31a68a7535f6068c4e14b95e90dcf@65.109.92.240:21016,157000d06040f2a7b981c6f062da0c9da0e6e6af@194.163.163.0:26656,be0522cbc5ea30f14355ff6d05ed4b9cf47d7dda@188.172.228.162:26656,95d0377592a657d4c0816d9845e11d659db75d5b@51.81.208.70:12256,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
