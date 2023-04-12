# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: orbit-alpha-1 | **Latest Version Tag**: v0.2.6 | **Wasm**: ON

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/defund-testnet](https://explorer.kjnodes.com/defund-testnet)

## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: defund-testnet.grpc.kjnodes.com:40090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (29)
```bash
peers="e494f017a60c9be7b73541ea9356affbeee1c9cb@178.18.247.73:27656,1e79c5a5da82a33cfb507089c028480ec455f24d@145.239.143.76:10256,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,86caf6297ae00fb58b58a272984275c592b2fdf7@65.109.84.216:56656,4171dcb48bd286ecdb2d83e67205c057ddaf5db4@185.245.183.55:27656,37fcbac03dec1b0b717faf074e76d12865884293@194.163.191.213:27656,e73a8c70a1e55c4ee14874c659a9084773ea56ed@95.217.104.49:36656,35bd24cfb2d71f1091b082376e8eab870a0496a1@65.109.82.75:46656,9f8ad11f0fcdd0bbbbbd4fcf54dbcd5e44db041d@109.123.243.13:27656,ffb2898494cdbd6625d962ea4511c29507177c62@164.68.103.176:26656,c1c6cf5859c43fb3acd19ccdb78a4caa0a151ff7@45.85.249.107:27656,6d18d29bd7be654b626ae2bdc4cc704e74cc1051@185.197.250.124:27656,035ff6d94b5c62d1830d71b25c259e11a679250d@38.242.158.116:27656,5c9a300d730e641ede5ab7125a3e455d93ab939a@65.109.50.106:27656,11d29b833c759f5595ffdb5d0652890a8972e0bf@185.217.126.168:27656,470e6c26996440acd257fb6cd24fd9dcd48a4f0e@149.102.136.188:27656,37c619f4073aff14ea579dc527fe9a6a8002d9e9@95.217.76.250:13656,773b4e59036c6934cdd3c919fc74259aba7d8ab3@185.16.39.4:26656,8c4bb6fac15cf74f5475cbc2fcb5ad5902ffa164@149.102.136.173:27656,eb7040eb80f3a0b62df828d38d818b3aec554b50@38.242.237.125:26456,20501e4b4d6eea8c2211e8da79c499549e5bb629@185.196.20.33:27656,6bb46db441cf84b5941717290a74ee8d853f0bdc@38.242.229.49:27656,789f5035190704fac04402363713179cb6c6ad00@109.195.139.31:26656,8e6c426f1b0052604cfbc8062e6ee73d3727e945@138.201.21.62:61556,790d14b181c9f538bfa81afaf70fe78c3e9b52e2@38.242.199.69:26656,b695113e075d522271c41ccb57b0a2c27e8ae346@65.109.160.32:40656,58437bc62307a512f391db5c1e24e3cff8b9f8d3@136.243.88.91:2070,f31bb89bdb7c2d7867872f9fbbdda3d3d6a9a609@5.78.44.148:26456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
