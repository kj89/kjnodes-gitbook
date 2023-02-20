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

**live-peers** (9)
```bash
peers="a03f2662a9520e34aee6fd561a8a126795f9420d@65.109.93.58:45656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,c5f6021d8da08ff53e90725c0c2a77f8d65f5e03@195.201.195.40:26656,e1ca2c14c007cc23e280b191d32b6a3da2389672@65.21.183.66:26656,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,334a842f175c2c24c6b11e8bce39c9d3443471ae@38.242.213.79:26656,29a9c5bfb54343d25c89d7119fade8b18201c503@209.34.206.32:26656,0a9c34419331688b0b40d50fddbee286927602cb@5.78.79.97:26656,44b9653567269c553fde91e75c78372baef24bae@65.109.27.156:32656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
