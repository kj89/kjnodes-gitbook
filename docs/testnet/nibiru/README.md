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
peers="cadf119fa38b4b211f819072ef754ab07d8b1dfb@77.232.43.194:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,49ee8e65e47d86799d26f54937304da04c2cc2b6@144.91.85.204:46656,2a333d36aa9c5d7fa0a4b143d6d33ed7c0336ebc@141.95.20.183:26656,fd1565e60c2baf3c35f62a16343168388cc419d3@149.102.129.164:26656,bbf891728d46b3df0702489aa0a3888c5e02843e@95.217.223.85:26656,b8c0312ad10f8d501c510a6d01f9c16ceaeb9114@144.126.147.39:26656,ba49814ebe24e4d1ba41f4fc774997bd5d7d8e47@65.108.126.46:35656,6feab732832b06516795938d585d1b77dc7ebbe4@154.53.54.11:29656,03de6cc7af9b236a28c319a7e792a681c7fe2205@95.217.211.58:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
