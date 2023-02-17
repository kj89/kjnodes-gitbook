# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/andromeda.png" width="150" alt=""><figcaption></figcaption></figure>

Andromeda is an application platform layer that connects all  public blockchains in the Cosmos ecosystem. Through our vast  library of no-code smart contracts, users can harness the power of web3.

**Chain ID**: galileo-3 | **Latest Version Tag**: galileo-3-v1.1.0-beta1 | **Wasm**: ON

[Website](https://www.andromedaprotocol.io) | [Discord](https://discord.gg/andromeda) | [Twitter](https://twitter.com/andromedaprot)




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
peers="749114faeb62649d94b8ed496efbdcd4a08b2e3e@136.243.93.134:20095,72bba2142c9cada7e4b8e861fb79e8a66e345d99@95.217.236.79:50656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656,f3d598517ea86c08236b53882338b0b5e1d0f0e8@213.239.207.175:42656,e1ca2c14c007cc23e280b191d32b6a3da2389672@65.21.183.66:26656,29a9c5bfb54343d25c89d7119fade8b18201c503@209.34.206.32:26656,bcdd1b337504f2d3523f6d63a7de1a2641187908@154.26.130.175:26656,a9d237b5070c7790a57318aa2bbe9b4f4f04cce2@194.163.175.163:30656,cd529600bb3aa20795a18c384c0edae2eb2da614@161.97.148.146:60656,bcef415d908dfc5c7caff3325eefd51a730695b4@65.21.92.46:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
