# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.1.0 | **Wasm**: OFF

Website: [https://www.defund.app](https://www.defund.app)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (34)
```
peers="aa0f97cda5bd962821b907245dc476348309fce3@84.21.171.33:40656,6afae0959c5ca811253c115a13f60b28e18c6ee9@95.111.243.139:40656,62df45d2df885de6dd2230dccf975a04005d23b3@164.68.121.197:40656,ca3658a2f24d0340e5eefce8c6c04e706188f407@38.242.244.56:26656,e4470dac98f2cee5bd060c52c7d801d57bfc9308@185.245.182.206:26656,6ad4f3be13155729927f0af19ceb08f89477798d@75.119.131.75:26656,d0c1ea8f3a3ad2d180fb3f1d166d53d8d397c76d@109.123.247.186:26656,0176c2127c25f0ecd8383577cd373e0928d20884@86.48.3.14:26656,cb503107b4135363d5ff83ff6a1a1423d8db4166@62.171.169.230:40656,e3d98694b276a2fa3bd52a77d00d379f0aacb58c@173.249.7.166:26656,5ac40e96d9194536e15a28a1010551300cbab616@185.216.75.21:26656,e84cc22dd9b951b9884f78cb184009cf25e4803f@54.90.149.14:28656,20b23961a22091e2a5047482d84bffacb49f416e@199.175.98.110:26656,195f80fa7d564efd62304bcb7da85f0a50f3d7db@109.123.254.113:26656,e89877d1394fed21805f7f62e61dc2f31f0e0110@149.154.64.93:26656,f94f1daf71e3c2dd06ebbab0c2061fc723f8b539@190.102.110.86:26656,989c2419816cc187213cd604d09b088b4d64518c@195.3.222.189:26656,d8e7d407f57383c4934ea116aadfa95eb46edea5@135.181.3.38:27656,028aa95415a9a004e57fd581d2c897f01a5b8054@80.241.211.235:26656,1b2746cea41c71c3062bfb22e686198fc39468eb@185.252.235.126:26656,abeb7b59282d3220aceca9b3a13c98021e6419a4@161.97.66.90:26656,313da8fe7d531d3c72a9b7517b1680f8bb715abf@144.126.150.75:26656,d2f1e1c40fd51098e62a5e4b003395767fd83fb9@45.87.104.74:26656,89971b6fbddaa8f7ffbcbc96176e152593e86f59@86.48.5.211:26656,e2542af1f83025786c34947f1b6d39a511500327@173.249.20.104:26656,cfd561edda42399f9a178f90d845063e756d6038@144.91.85.204:26656,5beca302247bb83bac77c18ac86ed01ec4d65f62@155.133.23.29:26656,bd90b1dd4ae3636e5f452be51b8e75ca104b5bfc@109.123.247.53:40656,d1976601f04df2a2c7e35c0e8212464acfb7512e@75.119.147.235:26656,04621fd537750900278a4b7e125c7d148ef8d8eb@130.0.216.207:46656,00ddc480c7373130e1086c54173ce2bc5e0e2d45@185.190.140.81:40656,ef9e0a0b1132925b68a57d1b3558439453708cf9@95.111.250.75:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,cf218ba3dd54fa9fb237351bc3fe90dd1264b5d2@161.97.72.7:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
