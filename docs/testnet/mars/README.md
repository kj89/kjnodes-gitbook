# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: ares-1 | **Latest Version Tag**: v1.0.0-rc7 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)


## Chain explorer
[https://explorer.kjnodes.com/mars-testnet](https://explorer.kjnodes.com/mars-testnet)

## Public endpoints

* api: [https://mars-testnet.api.kjnodes.com](https://mars-testnet.api.kjnodes.com)
* rpc: [https://mars-testnet.rpc.kjnodes.com](https://mars-testnet.rpc.kjnodes.com)
* grpc: [https://mars-testnet.grpc.kjnodes.com](https://mars-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@mars-testnet.rpc.kjnodes.com:45656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@mars-testnet.rpc.kjnodes.com:45659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars-testnet/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (10)
```bash
peers="e753c2dde523bbbe0981bea5708f267f63ae84c8@68.183.76.26:26656,8bb6ec79bc116c36c1271a2f5c14cd6c1e1b812f@65.109.92.240:26656,13066720a4fa7e84a2011580834a63c7c6bff59d@188.166.244.23:20656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,84f1325b17d2d0b7ed78c2f746c2bb515af37d48@65.109.204.197:26656,7ed60b9fdfc250a7a10bba3c539bce58c9533b5a@65.108.11.180:23656,e5577ecbf793ce92ce5993c4841a340a4c9db64b@65.108.204.119:46656,5dac2a64e4aea39e3704d551441938a504134e95@194.113.106.81:26656,92c3c938d39362d743c3d621619642fc81d5eb0e@91.230.110.200:45656,fe8d614aa5899a97c11d0601ef50c3e7ce17d57b@65.108.233.109:18556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
