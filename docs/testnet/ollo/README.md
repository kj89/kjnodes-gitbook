# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/ollo.png" width="150" alt=""><figcaption></figcaption></figure>

OLLO is a sovereign L1 chain built on the Cosmos network providing  next-gen trading tools & sustainable tokenomics.

**Chain ID**: ollo-testnet-1 | **Latest Version Tag**: v0.0.1 | **Wasm**: OFF

Website: [https://www.ollostation.zone](https://www.ollostation.zone)


## Public endpoints

* rpc: [https://ollo-testnet.rpc.kjnodes.com](https://ollo-testnet.rpc.kjnodes.com)
* api: [https://ollo-testnet.api.kjnodes.com](https://ollo-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ollo-testnet.rpc.kjnodes.com:32656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@ollo-testnet.rpc.kjnodes.com:32659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/ollo-testnet/addrbook.json > $HOME/.ollo/config/addrbook.json
```

**live-peers** (8)
```
peers="90ad9622ac54023fe4ee9824d77b5d3e3c25c245@162.55.234.70:54956,ad2b0a3dfdd52bb4de8624b6b378638815f8e64b@65.109.90.178:18156,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656,76035e4e4afa5d7e560c57f27bb147504cf33dac@35.228.89.235:26656,ab9ce6d100fd9fee4b0da8ad54d20e825e21e93a@188.166.178.146:26656,e5f7aed51914aa6a841535ee5760e0042524e297@188.166.181.125:26656,ee0e8fabb1b7d0511a2733b62ac68a7919896c5a@212.8.240.13:32656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
