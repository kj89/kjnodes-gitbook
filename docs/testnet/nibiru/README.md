# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:13990

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:13956
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:13959
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (19)
```bash
peers="a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,f98a8229e5dc6da6d5e49fd4e115472df3d1773c@95.9.36.100:26656,64fc94a56f69bae2ba8c23bfdf0f0c0ece535e68@184.174.34.119:26656,5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356,dd58949cab9bf75a42b556d04d3a4b1bbfadd8b5@144.76.97.251:40656,c414545b963134299a3c64a7d6386c9c4f7bd417@93.183.208.88:26656,613e133355a43be28b31d33d13c8814d6ea0c99f@34.75.8.154:26656,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,86a9ef837a37446469fc424b66e8fbf10d6619aa@84.46.255.162:26656,8a2e384b898a00dcf8052d129d6beb9f8f5ef86b@5.75.232.237:26656,74405e27923c1efe97fc678aa9f0357537a9b311@161.97.64.38:26656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,03833de20845507fd9c6d2ac1797d28ef4528b0c@109.123.252.252:26656,7f8bd4eaf6b9b213fd7b89ceefc517bcaa517d24@5.9.147.22:22656,acfb784350b9dd2558720d623fe25ac6fd4ac9d6@144.91.82.124:26656,fd5d54740618e8ca6d85cae52ec2db5ea8ac8ea5@91.107.196.77:26656,05b0e8da493f0be9fd94350da52fb59c54cc897f@161.97.150.23:26656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
