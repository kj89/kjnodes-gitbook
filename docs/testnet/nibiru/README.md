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

**live-peers** (10)
```
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,c5f3caef6a57b28b0a136c80c3b6165dd6d57fe2@65.109.27.156:26656,92e93ba4593eeed74988bab604df3fbc5426fc32@167.235.27.69:26656,54690dc01caf431dc46a2aa2e53664276cc8810e@144.76.30.36:15639,22e9680de9de88e4686c1705ee0ab8a08fb26cdd@88.210.9.78:26656,7633f5845c9d738e34315393ffb5bf1315549857@43.155.117.14:26656,8b476c96819a53d0ca785abb9d265ece651b5f9f@88.210.3.30:39656,5352e8b9f3a2d2606070e9b9c33c23b9afca5f06@62.217.187.39:26656,986d2c87f1e01b23a18aef2c52f68a6dc51da21d@194.146.13.223:26656,c880147e0f0980772010a97b8cbf949f12c0eb7c@178.18.247.78:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
