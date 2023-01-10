# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```bash
peers="c865b9d2e12a2388746aa69dda076db984e74c3f@104.248.249.197:26656,7182dfadba43a9a3b35f6862e63f75be20c8b1db@95.217.214.125:41656,eccdf1d5bf33bc1733838562b4d4a4a45869c3a8@135.181.183.93:41656,fb0a1c5dbc329b1b0ae3dac6776df4eb5f2072f6@79.137.248.142:26656,61af145c3cf74b80f2a7187a55499a3c97e35a8e@38.242.130.204:41656,5fa476e097bc0af605581b5fb905b10707c5762d@84.46.247.123:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,c78af3c8a2fa3d398dedb1ad9052eaf60dc27434@95.216.163.254:41656,b5fbf2633a1d00c4e0e62f1e0012f8e72af15aa9@185.218.124.169:26656,12f6b84a23b054a6591c647c2a4456c40af65cce@5.9.147.22:24656,6871aeacd353d66c38b1ebbf3b1ad244fa05e32b@167.86.84.125:26656,182a0faf787f0f62ac2af8975d951ab94573d7d2@194.195.87.52:41656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,29da5f642c71fe249f671c3632af2ec8d87785ee@147.182.255.64:26656,5b599e2470b01f8afa88448899f436130fb2e2fd@146.190.112.167:26656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,5c2c2b27e1824097d4f5dc7a581a8d615923e76f@185.252.235.110:41656,53b421af01f3260e949d6a9c2dc09e3b1dbf9fb6@109.205.181.30:41656,19fb417249992ae8def277fb753656da318fe250@38.242.133.239:41656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,4e0e57bcac8aa2bc3188d5b7845eeee61a61f3f0@194.163.170.165:26656,c5fa8b2df54c71b7a6479d9ba67dcd87b7109f25@103.104.75.230:41656,f97115243c6291081b546e8d59f51e5ecede4168@149.102.155.225:26656,38f4e436b28b05850fa9b67cadf0700123cec094@45.10.154.166:26656,33196fb0090d2de3671e36545d3425f641c9c0dc@65.109.70.4:41656,c19da021d6bbdeccdd03453a021d7171e6e299d5@173.249.14.30:656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,3b7845f8c8361c2f2de742473cd891c6e8cdeabf@83.171.249.159:656,d3fe4d63101e72c4cc5fd1114b57d36b759c0402@164.92.72.200:26656,6c938c9a9aeb2d6ab5f3c3695221a408f467a5d4@176.57.188.138:41656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,292c099fc654a1331d3b62a1b939f867b62ef434@45.85.147.242:656,995177c4b8c2b498de50483a614f9e30bf02e843@65.109.130.180:26656,3989c44e8af3427b22a71a94185e85df99d450b4@149.102.158.188:41656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
