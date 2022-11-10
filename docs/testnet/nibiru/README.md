# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-testnet-1 | **Latest Version Tag**: v0.15.0 | **Wasm**: OFF

Website: [https://nibiru.fi](https://nibiru.fi)


## Public endpoints

* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (8)
```
peers="b32bb87364a52df3efcbe9eacc178c96b35c823a@135.181.115.111:27656,968472e8769e0470fadad79febe51637dd208445@65.108.6.45:60656,0611817f25bd7e9cb3145278e419aa88de8f4751@167.235.145.69:26656,b1d022526a7040512ed0c91e8e20d9612e5e4978@154.26.132.217:26656,3cc4ba658dde90f2276455bb64a4efb666e1bc22@38.242.224.226:46656,7ce9e5d8ad9e4df2cd9d29ab38fff5275ad3b2db@38.242.141.224:26656,9732a620064660185b53352499584354dc8faffd@161.97.137.110:39656,726b928ba4aeb1303526e1a4efe1199fd25af07a@185.215.166.204:39656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
