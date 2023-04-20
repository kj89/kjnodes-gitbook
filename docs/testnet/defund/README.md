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

**live-peers** (30)
```bash
peers="da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,fb124c136c3aa20a71c68d9cb0a2833293c8dc58@23.88.73.158:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,0d2b4612c01b085e89b594a3db8f297b6bb6ba18@148.251.69.196:13656,b654f4b9394fcb6a98ca5845c70bb4026aa34fda@209.145.62.91:30656,0537a8d627b65f65c810206dffef9fa820183167@65.109.160.32:40656,6b94a3f12d8e694c3a735078e0cfa2b27940012a@95.214.55.62:26656,65b7c9a6fa81e532e701e9179b890b3038a86962@149.102.136.186:27656,86caf6297ae00fb58b58a272984275c592b2fdf7@65.109.84.216:56656,defccca5c186903b9979887dad9a5ee36c731e85@94.23.211.120:40656,6999cca6c55576a48d4f227b87dc904fbdb085aa@65.21.134.202:26576,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,e8ca3aa11355a1f261d74c6af4904d554c83ae4b@195.201.242.80:13656,2da5c563e31d3f3a0101f55ec6186d65465881d9@95.217.88.248:13656,64db984bc93ab23b3a1e2d8f060b56f1ef596b51@178.124.209.101:26656,0f69cbada28936e37e5413c2eefdcf1278fc96a3@178.124.208.150:26656,7b8af48c5c957a7b60d0772cbc4074211f50de0c@188.34.204.235:26656,33527195a479780ce40322433f1eca5d11bc47f5@89.163.140.70:26656,336d1bea02d11b52ebe81d22d20794b8d48fde13@173.249.7.166:26656,bc934501cffc27940d96e7775b6b8ae5122604ab@185.185.80.195:28656,e3c348467a8c88c0f65e2ca8a71875d2a384b8b4@185.16.39.19:60656,6047d282f126e8be4b36ca28c0cc3d244577f798@159.69.185.109:26656,1bb637816b9b28e428d515936d1d2cceb2d324cd@135.181.111.161:40656,195f80fa7d564efd62304bcb7da85f0a50f3d7db@109.123.254.113:26656,90f293a5f20979c5778ba6156597e7b9eb04539b@93.183.211.204:26656,1f993dfcf30d91c15437e8657b6020aea07f7632@65.108.232.182:13656,c1c6cf5859c43fb3acd19ccdb78a4caa0a151ff7@45.85.249.107:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,185401b61cbe26895b5a7c025e8666349c3129ff@213.133.97.154:13656,5c2a752c9b1952dbed075c56c600c3a79b58c395@146.59.47.207:26836"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
