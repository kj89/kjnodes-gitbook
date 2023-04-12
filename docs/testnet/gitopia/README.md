# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/gitopia-testnet](https://explorer.kjnodes.com/gitopia-testnet)

## Public endpoints

* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)
* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* grpc: gitopia-testnet.grpc.kjnodes.com:41090

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

**live-peers** (30)
```bash
peers="a6f4fd8efe8a575a15e25652ecebce3fa1ed62a0@213.239.217.52:35656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,7e0acc9368640587d09fe0b2ef9cba3549b0ba44@65.108.9.164:20556,c84906b19dc7dc7bda94ab2167d4b0af64a28b49@45.151.122.191:656,399d4e19186577b04c23296c4f7ecc53e61080cb@34.143.189.236:26656,c2beb74ebaf76137702732f6076c9a319bf15262@159.69.72.247:41656,ee812a11525cf7e2de4bd63e66aed8b8de337902@38.242.235.199:41656,d318a60a25b7a84322a8083709ff8e8bbe82ddb7@65.108.13.154:26656,1f0f03a1c845e810e5cfeb0d960639c637d049fe@154.26.131.130:36656,ac606e28c081c679dc23d9a94c29842be8f8b1f1@45.85.249.133:656,007d2419fea80aee707d009af0153f5105c53379@38.242.139.164:656,314ee8896c9f9e39450dc25623f8019cf316ed60@38.242.135.124:26656,5c45e8920c5094827ec5afaca9ab469aaa0b4eaf@65.109.88.254:28656,6ea375302fdd319ef64e013f469e286faf739da8@213.239.207.165:20086,f0b8227e40f25eaec0e25b9e91ca199d2d9a1ecb@167.86.94.177:656,b745e0c6a1e0c7ec248ec274cfd038ed4bc4c2cf@65.21.134.202:26356,9bb344d83fc1fafc4bce6b8e4a95b82f37ac4f31@82.208.20.136:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27036,082e95b5d5351e68dcfb24dff802f9064cfd5a4c@65.109.92.241:51056,1cf3826ccd9a24caa549cbea061446716858133e@154.26.130.95:36656,05182a9b6121c9fcbb493f9bb3843e20e076e479@38.242.231.113:656,8f5935761a8bc93c7eaf9fc8bb29b4b184269447@46.8.210.144:26656,52098a0fdd0dc566615ad37492019d252635bdda@45.85.249.131:656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656,7d39b009b329fc1a36457e814378872e67aef5c8@84.46.252.93:26656,f0a82f850a0da74c32836b125a52bdfd9a78fdd7@65.108.105.48:11356,c311e578c8b4e0f496f1d395473e74967c5b502c@164.92.197.50:26656,292c099fc654a1331d3b62a1b939f867b62ef434@45.85.147.242:656,eee5721079b6600954dbd01e1f2623d11d14e751@45.10.154.197:16656,7da6c90fe420bca73b5274884236134acf49d565@35.168.32.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.gitopia/config/config.toml
```
