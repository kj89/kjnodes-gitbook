# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: ares-1 | **Latest Version Tag**: v1.0.0-rc7 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)


## Chain explorer
[https://explorer.kjnodes.com/mars-testnet](https://explorer.kjnodes.com/mars-testnet)

## Public endpoints

* api: [https://mars-testnet.api.kjnodes.com](https://mars-testnet.api.kjnodes.com)
* rpc: [https://mars-testnet.rpc.kjnodes.com](https://mars-testnet.rpc.kjnodes.com)
* grpc: [https://mars-testnet.grpc.kjnodes.com](https://mars-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@mars-testnet.rpc.kjnodes.com:45656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@mars-testnet.rpc.kjnodes.com:45659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars-testnet/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (39)
```bash
peers="b9c1fb604f314a0b7340bdf2c44fa85ad67ed2ad@38.242.241.61:20656,cbe8b74723f5507fb12c81ac263f11eeda0f0c7b@65.109.88.178:26656,5bca99161a02e45e9e3fe6303728f8fd13d3d9d8@65.108.69.68:26757,ac73f0ba9b2111a83abe35cf12b361c360ce7e24@185.219.142.32:17656,eae08499096faf872ec686c0b5d66a7ad5ad510b@159.223.69.75:20656,e26ac62d4b4339bd8863c59027583c1f9a085675@185.225.232.196:22656,f7eee27edda4fad9a4ce6335d6adc9d5538435db@109.123.248.28:26656,2e84f06c036aa675a24a4242636cdda1639af800@20.165.200.238:20656,ffdbc710566c5e0d04846193e7bba100d2a737ee@136.243.103.53:33656,f1bc9d703500d54fdc2802552d2e31449028dea7@148.251.53.202:26656,f9855d1a7be36a228035358fc3ab7f3ce7353e5a@65.109.24.121:26656,2fb0eb08adb9ea1f7965efb65974948e8c234fef@116.202.165.116:33656,42f4f53d6ffb55662cf2b65396075f784a1e9a52@5.189.149.159:26656,ade06676777863cb7d360852616085761a68c544@46.4.53.94:26656,e5577ecbf793ce92ce5993c4841a340a4c9db64b@65.108.204.119:46656,bddf2a56b6783c6d79c46a07cbd707083677d4c4@135.181.183.93:33656,0a589d1ce953bb7acaaf5aa9002dfac36fc42649@199.175.98.136:26656,ed6bc9782a9cf2f5c302d8ecd5c53c27a3413e96@65.109.88.155:43656,a841d3e526089172867a73b709fd14e1d9fb87bd@65.108.231.124:22656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.53.233:27056,c5a39b97f56d73185ceb904899c65ad8d1390364@199.175.98.135:26656,14ba3b19424301a6bb58c27663a0323a81866d5d@134.122.82.186:26656,9c55f0518b9cb5c4000a7229707f00b787003757@192.99.14.194:26656,b1431595d4d661c5a1a4847d9ce18854a9c95d29@207.154.247.211:20656,66a77479d79a16e7cb0ba4702708e4554b40b5ea@176.9.146.72:43656,b0b0ae6d6ff4ca64de8281371f729796ac4ec5f6@23.88.70.109:33656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,7c7f52bf26d5ec2dcc9e016c0f521e0b2fe77fcd@95.214.55.25:26656,c5c50697d6438a5201ab460f38c130aed88fd214@212.23.222.126:26656,d79cd692ab2a4ef1a8be282cb398d6267b871b6d@88.99.164.158:181,09203a69a212cba7516c9928800fb7de4dc7b52b@159.69.138.47:33656,0dfb092da1c0f8abe4005d994ba1ef91f316c321@178.54.78.180:26656,a511f8a8a5ac801807417d3239a201ea7ec7d514@139.162.153.46:20656,c36d220f73090c242dc5e309695d2c379ee09462@188.166.218.88:20656,a446002f40b926db596deb7bae9ed3fe04af1c2e@65.108.206.215:17656,3b10cd500cebd27e9bae5a1ee1b5e8d9095ea6e0@139.99.217.221:45656,eab3633d86f723e46d3244a95ec3e5a89fdbb51b@67.217.60.198:11124,9e6eac82887f7422bc49651f8ffda6bfd2848f53@74.208.244.144:20656,dad74c1df2e15613ab64ce77bad20e13b131917a@142.93.207.43:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
