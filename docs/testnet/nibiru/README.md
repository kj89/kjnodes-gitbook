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

**live-peers** (22)
```bash
peers="a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,d622efcde775f33bd8c14fa5757ee9fa95d4149e@135.181.203.53:26656,cb825bccee49827c07dce19878c8790c67222a54@91.107.132.237:26656,db832cabda2d29d8e2570c0f3a5797098db5a7b8@135.181.25.101:26656,370107c2f46450646cfe87d59bd6684ec2231064@85.239.241.80:26656,0cc5236b8a37e89af65c8504982ae0eb5b01e004@178.20.47.61:26656,6173aa0fb340ab41724d72339d164a86e7a6d0ac@185.229.119.95:26656,595a8f93897710cacc3173c9ae4d0bafda5b3879@141.94.73.93:36656,4dbcf74d1c5760c2ef6037219c1c9b2e7a4cea63@194.163.137.48:26656,4e6bfe976a1f43c2368a8ec59a8716138b46227d@43.155.106.215:26656,20da1f2c82539b0e75e818d74cb3a3dd3f8e6b63@38.242.229.208:27656,7ef37c8952fdd9cfbf50aa7e89373876b28a3ed1@93.183.208.94:26656,7d3867934f0664832f782e3579e30686b069c473@109.123.250.109:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:13956,88e1a734951a8a4ea3f0b533d8bb49b9a5c24fde@120.226.39.116:16656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,ecbf8f3be0826e9905dc0dfff5c02d922cf768b9@65.21.56.168:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,ba49814ebe24e4d1ba41f4fc774997bd5d7d8e47@65.108.126.46:35656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,668ae8cb141c97d3fc27930bda216d94459e2790@135.181.253.203:26656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
