# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/zetachain.png" alt=""><figcaption></figcaption></figure>

An EVM-compatible L1 blockchain that connects everything:  Build interoperable dApps that span any chain including Bitcoin; access all chains from one place.

**Chain ID**: athens_7001-13 | **Latest Version Tag**: latest | **Wasm**: OFF

[Website](https://www.zetachain.com) | [Discord](https://discord.gg/zetachain) | [Twitter](https://twitter.com/zetablockchain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/zetachain-testnet](https://explorer.kjnodes.com/zetachain-testnet)

## Public endpoints

* api: [https://zetachain-testnet.api.kjnodes.com](https://zetachain-testnet.api.kjnodes.com)
* rpc: [https://zetachain-testnet.rpc.kjnodes.com](https://zetachain-testnet.rpc.kjnodes.com)
* grpc: zetachain-testnet.grpc.kjnodes.com:16090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@zetachain-testnet.rpc.kjnodes.com:16056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@zetachain-testnet.rpc.kjnodes.com:16059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/zetachain-testnet/addrbook.json > $HOME/.zetacored/config/addrbook.json
```

**live-peers** (27)
```bash
peers="24a3a8151ec9ecec0b9ed1ca97accfb1dacc115f@88.218.226.79:26656,d69a1868b953aceeeaaa2055f0af22c164774500@54.236.217.236:26656,7581f6a7b3913b900f172633df4e555342b350b1@202.8.10.137:26656,03ff657e528ab815721981e4ae5d2740fbf49df3@148.251.12.27:26656,af10c27ac4539b6c7f593013267d25797cf68ff2@54.187.106.246:26656,39871a19628e2fff0512f92d9304942093559720@135.181.115.175:26656,ab019797db848efb0823ab74a02c53c42b587981@18.182.78.42:26656,983972c8d76558b5f0150cd6bffc10ce4f608e4c@65.21.236.163:26656,eb9c277e7e17ecead4cbb8cc7b9483dcb1b585ad@15.235.196.87:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:16056,828a6e980767d83ee0d6eb798f6cadbad6446566@31.132.165.22:26756,a918d08544b5f4e0a9eb20bf91f343eb71b6d5ee@164.90.181.99:26656,5d7f8e723d1ba661d493fb11821f80017ebd621d@52.68.145.67:26656,e3fea0450f9d23ad7b64d41aab882a82a0b71d6b@150.136.176.81:26656,bf97dd85ee37256f2941c31b65bfccfc7198a969@5.9.60.44:26656,8ed2a97e44938fd2420018b6429d1c15164c65e8@178.128.232.111:26656,fe84af7cb024445566a44a332770628245ae3ded@45.83.106.237:26656,1ebb53ee60c8f4de0e2f24dfd1d8a5ff957b8b85@73.95.14.249:26656,1c1ab01057d9dc72665902f2b1d752714dbf6d24@116.202.227.117:16056,6a67ef86f77186d3462cb5075d7fd66713414846@5.78.100.162:26656,388f5fd1396bed6d962980e0f3adf1aa02689a7a@5.161.104.23:26656,bab6663f21b63e1df57ec7595b01ef1062dbd275@152.32.150.236:26656,b3fd5411d3e7984ea7bee8e83b0feec16f87311f@15.235.160.207:26656,809c1bdb33c162fdc380372523ccd58131368380@54.77.180.134:26656,a6090cdf3ff4bdc428ba89c4f622ec1b3490e338@18.143.71.236:26656,b96c038643c08373535956e3505a5aa955fadb0a@54.254.133.239:26656,af58c82b5f4d2268e0b8ca9150190e438c07d90d@34.239.99.239:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.zetacored/config/config.toml
```
