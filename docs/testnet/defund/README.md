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

**live-peers** (26)
```
peers="d2f1e1c40fd51098e62a5e4b003395767fd83fb9@45.87.104.74:26656,6ad4f3be13155729927f0af19ceb08f89477798d@75.119.131.75:26656,672adb4f349b23e7d408d9b01477eabe7523249b@178.18.245.208:40656,667f6c6d694bcd6743e6f42bb6e5996c4c9f16dd@84.244.31.1:26656,62df45d2df885de6dd2230dccf975a04005d23b3@164.68.121.197:40656,313da8fe7d531d3c72a9b7517b1680f8bb715abf@144.126.150.75:26656,a75589600b6ec065d6e830df49efb53e9c4ca036@95.111.252.92:26656,cf218ba3dd54fa9fb237351bc3fe90dd1264b5d2@161.97.72.7:26656,c640df433e42f07b2d2ea11679c35a69174f6ef2@194.180.176.124:26656,5a3e8478405460c847354dc3ab84437b51b2e50b@93.185.166.71:26656,9dd945f369a7aa1946e007d9547b364e69da7db8@185.192.96.140:26656,507e7ea5c2c97d411f66238b97d7e7d931800977@116.202.161.165:29656,bd4c137c54e4856b2d59d77dbd52b57e0fb7529e@149.102.152.61:26656,3f433acec2278166e82fa4ee9e4e73728e669cbc@144.126.146.134:36656,e2542af1f83025786c34947f1b6d39a511500327@173.249.20.104:26656,04621fd537750900278a4b7e125c7d148ef8d8eb@130.0.216.207:46656,748e7c000dc2fe6ac66686884f8533fc7916b6a3@38.242.244.163:26656,89971b6fbddaa8f7ffbcbc96176e152593e86f59@86.48.5.211:26656,e64fd30895fd003d110a7ac7b7ea7ef1214c6e53@92.63.194.210:40656,d1976601f04df2a2c7e35c0e8212464acfb7512e@75.119.147.235:26656,cb503107b4135363d5ff83ff6a1a1423d8db4166@62.171.169.230:40656,d0c1ea8f3a3ad2d180fb3f1d166d53d8d397c76d@109.123.247.186:26656,f94f1daf71e3c2dd06ebbab0c2061fc723f8b539@190.102.110.86:26656,cfd561edda42399f9a178f90d845063e756d6038@144.91.85.204:26656,13e13cc3b1cee183592bffc1aaae6a9b3b7a7e20@38.242.206.62:40656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
