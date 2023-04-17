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
peers="ed857708c330334e1e62751470d6ecddf0397459@65.109.69.59:12256,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,c3467e5becb108e62f6a6051eb5551e9f256d096@174.83.6.129:26656,bf0f5782650ddbf8121543b94705e5849f87120a@34.170.13.86:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.224.198.112:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,615ebc348998f7f050763dd0a9201e8f61e8fc07@35.210.78.199:26656,d36ac7580cc8907a00b0add8c3b047caea6df4ed@107.155.67.202:26636,fb8505c994cb90927c766e3c3d2db38044a596bc@139.59.31.201:26656,87a7a8cc67967d0ede5d68a1477c44a40a8705f7@108.165.178.242:26653,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,9854daeb5414cc415baaedc4cef000faf5e24f85@45.143.196.110:12256,0393c19b176d1cf8bc560c5a8fa990301deb1a7e@95.217.126.187:26656,186cc57831ec3f1b44066bcf485a9f1f0796479a@77.37.176.99:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,722884e3add85791c34a0563253dc47901320878@65.108.238.61:36656,a7d96dc929824613315dcc1c90fee119f28cc51f@164.152.160.155:26656,6cceba286b498d4a1931f85e35ea0fa433373057@78.47.208.99:26656,a424cd8cc8d5fdb714d3d93daeb10509b28c7e27@85.214.29.87:26656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,0198f6d3ebe7bed4d176558a2ce8d341531f3e7b@74.80.183.130:26653,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
