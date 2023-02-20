# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/wzM3kSN3sE) | [Twitter](https://twitter.com/andromedaprot)




## Chain explorer
[https://explorer.kjnodes.com/andromeda-testnet](https://explorer.kjnodes.com/andromeda-testnet)

## Public endpoints

* api: [https://andromeda-testnet.api.kjnodes.com](https://andromeda-testnet.api.kjnodes.com)
* rpc: [https://andromeda-testnet.rpc.kjnodes.com](https://andromeda-testnet.rpc.kjnodes.com)
* grpc: [https://andromeda-testnet.grpc.kjnodes.com](https://andromeda-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@andromeda-testnet.rpc.kjnodes.com:47656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@andromeda-testnet.rpc.kjnodes.com:47659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/andromeda-testnet/addrbook.json > $HOME/.andromedad/config/addrbook.json
```

**live-peers** (10)
```bash
peers="1d94f397352dc20be4b56e4bfd9305649cbac778@65.108.232.150:20095,bd323d2c7ce260b831d20923d390e4a1623f32c4@213.239.215.195:20095,e1ca2c14c007cc23e280b191d32b6a3da2389672@65.21.183.66:26656,29a9c5bfb54343d25c89d7119fade8b18201c503@209.34.206.32:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,c5f6021d8da08ff53e90725c0c2a77f8d65f5e03@195.201.195.40:26656,7ac17e470c16814be55aa02a1611b23a3fba3097@75.119.141.16:26656,0f966c78a7ac4722bd389f5c010efb8235ca8f73@65.108.227.112:14656,749114faeb62649d94b8ed496efbdcd4a08b2e3e@136.243.93.134:20095"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
