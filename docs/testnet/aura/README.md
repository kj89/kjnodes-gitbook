# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/aura.png" width="150" alt=""><figcaption></figcaption></figure>

The Aura Network protocol allows users to mint, rate, track data,  or trade NFT for the goal of constructing a strong platform to  support all trading assets on the crypto market in a simpler and easier way

**Chain ID**: euphoria-2 | **Latest Version Tag**: euphoria_v0.4.1 | **Wasm**: ON

Website: [https://aura.network](https://aura.network)


## Public endpoints

* rpc: [https://aura-testnet.rpc.kjnodes.com](https://aura-testnet.rpc.kjnodes.com)
* api: [https://aura-testnet.api.kjnodes.com](https://aura-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@aura-testnet.rpc.kjnodes.com:17656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@aura-testnet.rpc.kjnodes.com:17659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/aura-testnet/addrbook.json > $HOME/.aura/config/addrbook.json
```

**live-peers** (10)
```
peers="d78b491967003bf1c509732b0a6a24169ccf75dc@195.201.165.123:11046,2e1407476ad3566eb11ac92ad1df4782c7ba83dd@18.143.61.108:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:17656,b8125bee4bc07c591dfa0e292d18a800d28fabef@65.21.139.244:26656,3d6b07bdb11754c8c8512525dac109d8bdee3857@65.21.53.39:7656,5b2758dfcbcbc19b9a0ee04c09008b67c98cd7d9@162.244.35.40:24656,841fa4f52671cc02f9a817a6d4a4522cd9a049a6@178.170.15.31:26656,f4047b504d4d5faa47a9044ab48bd29837051d79@5.161.141.144:26656,0770c2687cc34d59ca62270960d3ffcad6e42cf8@65.108.233.44:21656,7812205773ac30f3d47200ac2391c79896c60135@54.254.220.113:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.aura/config/config.toml
```
