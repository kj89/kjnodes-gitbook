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

**live-peers** (29)
```bash
peers="a424cd8cc8d5fdb714d3d93daeb10509b28c7e27@85.214.29.87:26656,5dbe792854b8f81df6c6fe5b7aa64d60b27f6100@137.184.235.212:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:16656,9ed4a1c80960ae933551283eb8aef52468f6cfc7@65.109.106.169:26656,97e4468ac589eac505a800411c635b14511a61bb@169.155.171.184:26656,aa0d47509ecadb630189fe4ef071d438a6493e69@178.162.165.194:24095,ade7d4d0009c7725ee991b8c40a7f646f76bf1e3@149.102.140.108:26656,186cc57831ec3f1b44066bcf485a9f1f0796479a@77.37.176.99:26656,c3467e5becb108e62f6a6051eb5551e9f256d096@129.222.220.244:26656,44e797771bff124693e63a8ec331d42873cf2ae2@95.217.202.49:35656,1483ddbd1ba369c01d5496877314ed1b09bd9cc3@65.21.189.221:12256,ed70fb7322fda1ee4646df34b47919ec6728586b@96.234.160.22:26656,ea6a7b2f366bc343f0670f1673fd86001dd08eb0@65.108.122.246:26636,ebc272824924ea1a27ea3183dd0b9ba713494f83@185.16.39.158:26886,bdc2baaf2d18152c38340d368249ac866daf3e3d@198.244.178.213:26656,54672e848a31d2e7aeda35b8f2c320ad508c5550@128.199.141.132:26656,bba10290da32f3cb41e15c3a192413666ce05cee@136.243.119.243:26656,04b797b5a56fb939a97a3c7d9c3230d09b85e8d7@93.189.30.118:26656,9854daeb5414cc415baaedc4cef000faf5e24f85@45.143.196.110:12256,cd680cc992983e5c8244b5529034a2e362e7a6d3@93.159.134.157:26656,8602d85bc570686ef255370177a92569e1ba4aa2@54.38.38.40:26639,d041196a1a36091605448fc65181408ccc1d5da1@65.109.122.105:61156,a206a5ff59132c3f771735dec337432e6cfb2f7c@15.235.53.45:2062,6831d67983cf5ebcb44da01737ccd6ccbd15c08e@193.70.47.90:12256,9ee75491e354965d8bfd8434aa093f8613bc1dce@65.108.238.103:12256,befab97d41e02ea4e759eda3de9e30e77b95b55b@35.224.198.112:26656,222b5f1f8f8b4933c1913818ab2b7379c282b4e2@65.108.75.107:11656,8fff37214fb0ef622f1c09dccb22d6321e004c3e@109.123.242.163:50056,8e4e1f1e087c76c71c64e477e95495833da82aa2@135.181.173.139:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.stride/config/config.toml
```
