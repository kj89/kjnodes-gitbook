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
peers="63f84e13148befd235d28b3e46b1de2da0aa99d8@176.9.167.181:26696,e734f373258a3c12d8c89a99e7d1124efc93ecab@185.250.148.41:26656,aee330dcdb120bc2b413feb513386296835cf545@62.171.150.36:26656,ded2aa043bd924c1f36151ab749b59b5749037a3@135.181.98.169:36656,5a1977f1db820b7ee4719abbbff6f721f14176eb@65.109.84.254:36656,c55bf5597637964690e4255c1e78d81d848ca51f@65.108.252.216:36656,09f8d04b89d6ed15e216a4c7f5469f42d5b90f9b@195.201.241.25:40656,edabbcbfb21c488be785f0925b0060c717440bad@92.119.112.229:26656,b1e1758323425265c1db42b0fbaa7ab80612a582@38.242.207.15:40656,24be58ab07ed513a64b359174c6bb6a17fa112d4@65.109.17.86:41656,ba7d98b76435f2dad0b499429b730b817ddf85e1@45.147.199.214:26656,f9fcb1705d112b357fa498bb0711e2f4953d3f88@195.201.237.188:18656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,3441bf28387afc7d9b6e7a754c3ed37f21006859@5.161.134.231:26656,409d5422d6934b0dedfd3347e078b67aac691120@45.147.199.185:26656,bef3701487b54ba73de5e0d84ac57fc2a54f3a5f@45.147.199.67:26656,57eadf177e7429db82bfdbed6fa0521e8741e404@94.130.13.40:26656,0484eab6881ba458c5988296403963aaf273700b@157.90.236.25:18656,00ddc480c7373130e1086c54173ce2bc5e0e2d45@185.190.140.81:40656,d1d1f9b34c3e4d46d7268588848b59b3a696a533@194.233.66.70:26656,1ca28a7348da501a1d92656123692af8f9f85732@45.147.199.39:26656,4d2f9132892d172b79cf00937fd554bd0f6a263c@92.119.112.200:26656,9ae365f1c4a2b95c95fdcaa92db4a4f5a655ef1f@5.161.108.72:26656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,9c55522cc229ca89724d432f394374f1aa5269db@5.161.59.190:26656,028aa95415a9a004e57fd581d2c897f01a5b8054@80.241.211.235:26656,0e5c41bec481ae4da0577377bc1952eb29b1e4c1@65.21.78.86:26656,e73a8c70a1e55c4ee14874c659a9084773ea56ed@168.119.227.28:36656,ec80e423e75ae61ecd24bf29f0a9b0720070e074@78.46.106.75:26656,77a7c437c7e0c421eeaebe677235306d2466da4c@91.194.11.156:26656,67742399a48abc97c7eef61b1a60b96c720122c2@45.147.199.180:26656,62df45d2df885de6dd2230dccf975a04005d23b3@164.68.121.197:40656,90dc33a14889c0a0348b18a03d2a3d0eab41e6cb@92.119.112.225:26656,2b8e2f05af0b716b551e2d0280090cbe86316a75@124.223.26.171:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
