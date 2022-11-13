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

**live-peers** (9)
```
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:19656,31413c99357d0cfc48a46767ade171db2ea0205e@135.181.138.160:46656,b43fd626841df11d1b397ef51f1919824d6ff258@88.198.39.43:26696,bf100c1b6b44a6e96ab5691f3023cec3c27747fd@144.126.142.78:46656,5ae1012f9b0f4672d8152de903d115dd2f1a3ee3@65.21.170.3:27656,a97eb7a4f3d857f1ff82265d2905fc0762a6bfd4@135.125.5.31:54256,00f496b62187a50f8ba353e2e6a7c5c4746ce968@65.108.9.61:26956,b210513cff3daa334acfc8df733944facc1b061f@38.242.216.207:36656,ccc59b8a55f9c6e7a24bd693e2796f781ea3a670@65.108.227.133:27656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.teritorid/config/config.toml
```
