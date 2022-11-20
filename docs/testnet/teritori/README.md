# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/teritori.png" width="150" alt=""><figcaption></figcaption></figure>

Teritori is a multi-chain hub designed to allow IBC and non IBC communities  to connect, trade services & NFTs, launch new projects & build further existing ones.

**Chain ID**: teritori-testnet-v3 | **Latest Version Tag**: v1.3.0 | **Wasm**: ON

Website: [https://teritori.com](https://teritori.com)


## Public endpoints

* rpc: [https://teritori-testnet.rpc.kjnodes.com](https://teritori-testnet.rpc.kjnodes.com)
* api: [https://teritori-testnet.api.kjnodes.com](https://teritori-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@teritori-testnet.rpc.kjnodes.com:19656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@teritori-testnet.rpc.kjnodes.com:19659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/teritori-testnet/addrbook.json > $HOME/.teritorid/config/addrbook.json
```

**live-peers** (10)
```
peers="c56b132be41b247c9f8fa1f2addaca57f9946e29@75.119.159.159:44656,ec0c58dbfe67a12ea16951134e29a6566ac05add@185.217.125.98:26656,53f69cd52a4b633179b9e762cf8d51f6696a27f6@51.159.141.148:26656,e1c50c477202e2f37643d044a6cde3c913f42230@65.108.71.92:54256,0e51ebd10636b48b69625677a5154b839ff3f557@65.108.43.116:56107,356fbd3263e387bea0528ac4bbbc89a83d52e9fa@65.21.134.202:26736,a97eb7a4f3d857f1ff82265d2905fc0762a6bfd4@135.125.5.31:54256,72266bdaf896279db491c333680d1a277944a3c4@65.108.194.26:46656,31413c99357d0cfc48a46767ade171db2ea0205e@135.181.138.160:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:19656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
