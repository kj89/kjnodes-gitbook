# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/stride.png" width="150" alt=""><figcaption></figcaption></figure>

Stride is a blockchain ("zone") that provides liquidity for staked assets.  Using Stride, you can earn both staking and DeFi yields across the Cosmos IBC ecosystem

**Chain ID**: stride-1 | **Latest Version Tag**: v9.0.0 | **Wasm**: OFF

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
peers="711030caa133cdcbf4aa357216279cbbb843b7f3@51.79.19.15:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,3505b1ece40f94cab8f80cfe31f5106c028ccd05@185.193.17.40:12256,d95477fd745d8a5e4b3d9052149d28a5dc447a88@35.206.158.54:26656,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,018d66466cfd907d5cc166ba3d5df8958c96e80a@149.56.36.205:26656,c938bcc723f004798750c3c533e8a6735f6d8363@38.146.3.122:12256,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,3963b7cd5230ae2ba6800375421982d535a133e3@35.79.215.251:26656,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,615ebc348998f7f050763dd0a9201e8f61e8fc07@35.210.78.199:26656,aa0d47509ecadb630189fe4ef071d438a6493e69@178.162.165.194:24095,59e886de6617994e8041124fecde40ab2ebae9e6@45.132.244.233:26656,48ab642db71cf3620a04ee15078b8a23bb443ae3@65.108.227.43:26656,cfd27429d382ecf366ddad02c88f15a8753092c8@66.172.36.135:28656,754b74f0a4208fcb80945a02c3a2826f7be4e763@144.91.102.95:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,cc35475fe1f7c345af0ea8a692f3b4b41c8f12a2@116.202.36.240:10156,3023b940ec9a39661c95877cec99e17416dc2a17@51.89.6.150:21656,9731c3365c772b3bc4580de5708a33f22c6174ec@208.102.87.76:26656,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,20f56a68a04eedc764b7e1b87b7032a50b9d4fe9@51.81.155.97:10456,e41dd510feb9e14df82ce0f4eab258fad78645ea@158.247.218.149:10002,d056dcd5ac8dddb23e2962a5ade6ee51f9bfd785@162.19.89.8:10456,aa28a50f877a8d60c52f42d15d14ffa7ef8639c3@5.75.188.247:26639,a1f479dc2e3322c6547a39c6c7eef5a191def57f@34.66.206.221:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
