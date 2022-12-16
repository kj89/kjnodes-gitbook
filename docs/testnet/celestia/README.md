# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/celestia.png" width="150" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: mocha | **Latest Version Tag**: v0.11.0 | **Wasm**: OFF

Website: [https://celestia.org](https://celestia.org)


## Public endpoints

* rpc: [https://celestia-testnet.rpc.kjnodes.com](https://celestia-testnet.rpc.kjnodes.com)
* api: [https://celestia-testnet.api.kjnodes.com](https://celestia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@celestia-testnet.rpc.kjnodes.com:20656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@celestia-testnet.rpc.kjnodes.com:20659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/celestia-testnet/addrbook.json > $HOME/.celestia-app/config/addrbook.json
```

**live-peers** (34)
```
peers="5273f0deefa5f9c2d0a3bbf70840bb44c65d835c@80.190.129.50:49656,e7dc98812ba79276f045ed080a6910540ce37e2a@159.69.241.155:20656,78091973241d5638259f518f3b19f6320b7fb451@135.181.119.59:20656,3c3347474b104b38a16f98c4bc09665199bb6741@142.132.211.91:20656,77fe717fc70370c5b1782c136a5bf7ef1e1e7b5d@167.235.233.34:26656,0d8b40858dcdf1e4370b2ed66b632bddf13a150d@75.119.143.147:26656,40e062988c54671aa7a55c6efaa73d3c0ae4920a@34.133.218.0:26656,6a03b088a9e183e7faa897afcc6b50c6971a4cd5@159.69.5.164:26656,eec289755259106bf29266c401bace003289c6be@35.234.94.146:26656,f635022d319d71bc91c3080fe3bda7bc3a68b55a@116.202.227.117:20656,e286b562eddc6fea1b2635f6623430225666fb2f@147.135.144.58:26656,38553b85b8740315da067fdd28a195c45df9069b@148.251.11.99:20656,f3cb453d959059440c3abe2bb07a692b3f77e5a0@135.181.248.87:20656,1d667e973e0dfcf0f92f7a202c241f5cfa6039cb@188.34.154.35:26656,3ad7f2d36f5e15d902c7aff7a305bea40f03f95c@163.172.111.148:26656,002fc3b88ec74753e2539bf30828e7f8bd19cc65@35.220.185.86:26656,e6c28bd7cb4be3651942a9d93368651c97ee4733@65.108.65.36:20656,e074e923e1c69e4ca86c1b002c4886b422ca5dc6@135.181.183.93:23656,42b331adaa9ece4c455b92f0d26e3382e46d43f0@161.97.180.20:56656,f98ee535cea1baf4a8fa438d1cd4e69ac836791f@65.21.234.47:26826,3ccaca3a32779bcf4c5cc85aae66a46902f0b641@95.216.223.149:26656,95ee0ec383a1a8773f0a8966c5e04b537facc92b@5.9.81.187:37656,c63069c8f462825d96631b2f34283936e015757f@80.82.215.19:36656,8262231964896250acd4e8171663f59bd53d7a91@5.161.80.30:20656,e0c364f5bd46d111ab17c370203f784140fd0466@116.203.35.82:25656,cb0db7a1fb8897c8eec9b09285e39d1756ed87b7@65.109.88.254:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,2c93920515e53e0e08ca4bc86dd76a194ee34a29@89.117.59.233:26656,a5f31a5c2c0469cc9b37b18528471f0ed867e747@65.108.105.36:20656,70ad1e4808ad49f192f3536cf180aa22ca804fc6@34.88.189.48:26656,5aea20b40e68bcfaf856cc2d47480d9a8607ae1f@135.181.251.100:20656,ca40b8ccd7c9d717ca691a74bec1e67aa9ae72c8@31.223.32.35:26656,70a4fcccfc02c8fc0172dd97def0e9d597ffa343@38.242.128.250:26656,28efe591fb72a460969c58a751b4b18a961ed7af@34.125.152.220:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.celestia-app/config/config.toml
```
