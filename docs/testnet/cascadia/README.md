# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:15590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:15556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:15559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (11)
```bash
peers="6f44ab7ad9d6a4366a80c8fd8f904e6ab2f6e535@5.9.48.90:26656,780b02fd73b698834c4cdd0c7d7123586b71ece1@209.38.243.102:18656,ef0b3d1c9908c34d76247ee520087d2892395586@167.86.88.130:26656,6452c82f6e479b764a23a5886855cdd67ba0d01b@84.46.247.94:26656,bf6898adad4d66e363974d9fab1e8199f05d0aa9@135.181.132.176:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,717deddb07d6a6990d876bf3d9bf974ca30223a2@173.249.53.21:656,4ead67f38f3163a5c849333faaaf760b6d9eda8e@185.237.253.88:26656,dd6836e921c1ddc7b87d8c3dd87929dab80a9aaf@77.105.138.110:26656,c94df794fdee1bf67ac7789a50159390c1580530@38.242.221.76:26656,d3e1ce95ac1e2830296eff1c952b89d6c3d84f7a@217.197.117.53:61256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
