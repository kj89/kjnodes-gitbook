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

**live-peers** (10)
```
peers="0bd4dce54aad2d9b67b992fd69b51694b43d3272@149.102.147.59:32656,ad204b3422acb2e9a364941e540c99203ec22c5c@212.23.222.93:26656,ad2b0a3dfdd52bb4de8624b6b378638815f8e64b@65.109.90.178:18156,4a1dce5e59374f85d45fdb49478658b03e3d2ef3@65.21.134.202:26626,d6c5ff021b091a1fd93b9f811cf7fca0d31e8510@65.108.238.61:46656,ab9ce6d100fd9fee4b0da8ad54d20e825e21e93a@188.166.178.146:26656,d14b740968d24aa5c31ade7dbda2b1204c40f24c@65.109.52.156:46656,5b2e5dbcfd31d4ed97ea6b4cda76155841bf47f1@185.209.228.174:26656,9865c6e15faced6643adc228e3a59744e1b4e277@116.203.29.162:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:32656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.ollo/config/config.toml
```
