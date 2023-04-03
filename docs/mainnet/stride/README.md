# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stride.png" width="150" alt=""><figcaption></figcaption></figure>

Stride is a blockchain ("zone") that provides liquidity for staked assets.  Using Stride, you can earn both staking and DeFi yields across the Cosmos IBC ecosystem

**Chain ID**: stride-1 | **Latest Version Tag**: v8.0.0 | **Wasm**: OFF

[Website](https://stride.zone) | [Discord](https://discord.gg/mzQZ8dAE7u) | [Twitter](https://twitter.com/stride_zone)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/stride/stridevaloper1j8gkhtllnp252l6g6zwzea30e7pvzqttr9768n)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/stride/stridevaloper1j8gkhtllnp252l6g6zwzea30e7pvzqttr9768n) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/stride](https://explorer.kjnodes.com/stride)

## Public endpoints

* api: [https://stride.api.kjnodes.com](https://stride.api.kjnodes.com)
* rpc: [https://stride.rpc.kjnodes.com](https://stride.rpc.kjnodes.com)
* grpc: stride.grpc.kjnodes.com:16090

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

**live-peers** (30)
```bash
peers="a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.155:26656,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,a7b4cf6f65138ba61518c2c45402da32dc8e28b7@88.99.164.158:21016,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.187:26656,166da4de977381ea8853986be11dbb470d9dc2ba@149.202.72.186:26639,05eec003db41d7ff47a317ef59f83e31bdca23c3@78.107.234.44:26656,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.224.198.112:26656,a424cd8cc8d5fdb714d3d93daeb10509b28c7e27@85.214.29.87:26656,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,7ec6917a0519decec00a9a29f599c4d90ebf3b86@65.21.136.170:51656,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.139:26656,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,c938bcc723f004798750c3c533e8a6735f6d8363@38.146.3.122:12256,d77e7918b9f9e21ee60a8e03075ca3e5f7353912@162.55.4.253:26656,e821acdaf0c7a3c60ea3cd4eb4a98a62dad06f58@43.201.12.41:26656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,fc305427390397f8c4eebe5bc22919c1cc5d4532@65.109.43.75:27007,87a7a8cc67967d0ede5d68a1477c44a40a8705f7@108.165.178.242:26653,e1b058e5cfa2b836ddaa496b10911da62dcf182e@138.201.8.248:26656,0198f6d3ebe7bed4d176558a2ce8d341531f3e7b@74.80.183.130:26653,233e06cfa51d53e186afe032e848f5c9f5cd4a01@83.171.248.3:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,fb24bc1de8c563e822897fba89bf150c602f3123@198.244.178.213:26656,2254e6968e5c7ebc98ef5b79b388502fa44e10e1@5.161.134.44:26656,6856de6f0c70a850db2b58deb43d568fced4a524@165.227.208.6:26656,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,9854daeb5414cc415baaedc4cef000faf5e24f85@45.143.196.110:12256,471518432477e31ea348af246c0b54095d41352c@78.47.210.211:26656,ed857708c330334e1e62751470d6ecddf0397459@65.109.69.59:12256,0003bf00c79e8ebd1f31c0f83ad3d181f97f98e9@62.109.17.96:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
