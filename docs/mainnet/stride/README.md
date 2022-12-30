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
peers="a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.155:26656,ec3ab92c9635230e6262fa7d9293452d8130fc12@5.161.99.247:26656,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,e37c0178e07c5de335c0e6293fec39b473e7f1e1@65.109.52.178:26656,4f9e3239a2bbf7d30ec9c0e5271a6f87fe6b3257@65.108.135.212:16656,df1d522512419a563615ed3708abf928f0fc5080@137.184.134.126:26656,1e0e88fac793f68822d3ea8e952f2dc0f4c1ca57@142.132.135.125:20656,b6bbf3fce8563bf55cee37776d1cfc3e6692c7e6@167.235.1.101:26656,6856de6f0c70a850db2b58deb43d568fced4a524@35.208.90.201:26656,8ade90b45b991088c92e8583e8bc93589d6cd81e@84.244.95.247:26656,28db7a664e95241930c5680ad2e1480bed3fb99f@198.244.178.213:26656,463b1dc6903455575079572fb23407be586f2a4b@185.16.39.37:26656,a757fc9ea95a7f643d392ec9fdaa31cbf06e76d9@195.3.221.21:12256,5093547fdf0430143ac66b4ee55d80e6542a6c10@217.174.247.163:26656,ed857708c330334e1e62751470d6ecddf0397459@65.109.69.59:12256,d77e7918b9f9e21ee60a8e03075ca3e5f7353912@162.55.4.253:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,182d866c8be094dffad6719702ff2514b5dfeabb@54.37.129.164:54356,4d17c6e85a1e6282efee950ff3dfe85b4b043f0f@148.251.51.144:26656,6a6a70719d44dfdaa74a074f017dc1f1ff23da62@146.59.0.123:6000,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,157000d06040f2a7b981c6f062da0c9da0e6e6af@194.163.163.0:26656,a3f95b0b15c31a68a7535f6068c4e14b95e90dcf@65.109.92.240:21016,a2128f5552cf4ae60a769999c7fddc5d9d44d149@15.235.42.151:26661,d5035bd01baef508402b8649a33afc7b0fd190f1@141.95.72.74:24095,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,8d7d0f32d53467c4d5e8871faf4ec58ea970fed2@157.90.179.182:26456,1ec2a654e00e22279ee50f13f074f2bce7218681@15.235.114.194:10156,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,e821acdaf0c7a3c60ea3cd4eb4a98a62dad06f58@43.201.12.41:26656,2c1f55e905c7425f995947e2d600ca5ac863b8c1@15.235.53.91:13456,5e0250a806113d60be48fab434ed81bb3e41be13@192.99.14.194:26656,068dd2e01b16710469518eefa42417425a17ffbe@54.196.249.249:26656,777274fb08ed48a4e027664e2576a8460272e43c@15.235.115.153:26656,d2247f7b919f0781c90ee61958d7044665a22d38@169.155.44.213:26656,f5732d5a406bdbbf08acad017c0993c0aa8ebe70@34.145.16.183:26656,7ef5ff00fe94933b8ba4b7ae4a8632ece5db11df@35.203.189.148:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.stride/config/config.toml
```
