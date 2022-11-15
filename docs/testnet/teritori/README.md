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
peers="9d709483ac8dbbe4adf19eb1b4732531254a2045@116.202.236.115:26656,3b539b6cff93fb3631d0a600a56ade3c6ca6bea3@141.95.104.33:26656,31413c99357d0cfc48a46767ade171db2ea0205e@135.181.138.160:46656,c56b132be41b247c9f8fa1f2addaca57f9946e29@75.119.159.159:44656,a97eb7a4f3d857f1ff82265d2905fc0762a6bfd4@135.125.5.31:54256,53f69cd52a4b633179b9e762cf8d51f6696a27f6@51.159.141.148:26656,0e51ebd10636b48b69625677a5154b839ff3f557@65.108.43.116:56107,ccc59b8a55f9c6e7a24bd693e2796f781ea3a670@65.108.227.133:27656,b43fd626841df11d1b397ef51f1919824d6ff258@88.198.39.43:26696,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:19656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```