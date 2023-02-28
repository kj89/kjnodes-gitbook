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
peers="360ab15495b087bc27d134418dcd9191dec07c12@46.175.148.142:26656,df7cf95427701d6d00797042fb8548a7f8eeeb6e@172.104.159.69:55716,093a6c911937d6d870780003c2b0a39c050d9d85@194.31.109.199:26656,91fde61878d704917f882694b271b67a38865ddc@149.102.142.94:26656,29a9c5bfb54343d25c89d7119fade8b18201c503@209.34.206.32:26656,0fd8550e58b1e450b40032e17ca6d685f7be1c53@217.160.201.92:26656,66e4051cbbfe428d64b6bd615a7e77b3c4f1ca61@185.215.167.133:46656,00cedd85b1f6a2c859a8c6116b9578e1cc2623c6@51.222.44.116:30656,f51b215535e43428b7122c3d3ebbb4ab20c1b808@185.9.144.138:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:47656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.andromedad/config/config.toml
```
