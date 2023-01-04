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

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```
peers="4977214dacb3713797653c1bc07b5982bcc91649@142.132.253.112:51656,c2beb74ebaf76137702732f6076c9a319bf15262@159.69.72.247:41656,648416f708c52248a00c5ad3912387a353c26548@178.63.102.172:44656,35c829910f80387ee825da9fb69efbcbf8e2149e@164.68.118.227:26656,98c3458ef7182730c6402f7f582eef2f77578b8c@185.250.36.151:41656,921348b18868c83bfc5375fc9860bb28aaaf0d0e@38.242.238.229:26656,6c938c9a9aeb2d6ab5f3c3695221a408f467a5d4@176.57.188.138:41656,edae8278cef6113e38af80504fb83cbf5eb0f023@165.232.129.242:26656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,31af09cf452ded09a5b3ffdab49efc4248feaca9@143.198.69.150:26656,995177c4b8c2b498de50483a614f9e30bf02e843@65.109.130.180:26656,61d2b313e2adc9d7990944f8ab5a6f9ecf08084f@65.21.122.171:16656,5c74fe6868cda2003926c0a6299c9cebec5c4d1a@65.21.239.60:41656,fb0a1c5dbc329b1b0ae3dac6776df4eb5f2072f6@79.137.248.142:26656,d3fe4d63101e72c4cc5fd1114b57d36b759c0402@164.92.72.200:26656,996e783f3df1e83e0886eac6c7dc4af451e87fc5@95.165.89.222:24136,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,9385d79528cabb5f855a02dba8c88a2d430e824a@164.68.124.151:26656,374da78901e59810277fc35482bce6e30953f488@80.79.6.155:41656,481189b7e246f6c824a969482446c49abbfe76b8@161.97.172.147:26656,292c099fc654a1331d3b62a1b939f867b62ef434@45.85.147.242:656,426863534b14513990b6b9dd2d8e085993c326d4@161.97.145.13:41656,016b0e565abd496b9473b87ac41339251005d12e@194.163.167.163:41656,95203479677e2ab00b1fb0bc1359294d4612e684@85.239.231.0:26656,19fb417249992ae8def277fb753656da318fe250@38.242.133.239:41656,53b421af01f3260e949d6a9c2dc09e3b1dbf9fb6@109.205.181.30:41656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,407eb21b784f1dc4e9902cb812b65eec760c6a19@185.193.66.67:656,4ceba74efb843cf10926a9ec757e4e2081d71e92@207.244.226.183:656,6871aeacd353d66c38b1ebbf3b1ad244fa05e32b@167.86.84.125:26656,e511a5b55979b7d630f016e2b15b513690fd3e33@185.239.209.124:656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,e189c585d02d81a91112622c6c7ea3f6c8c7a591@64.227.98.226:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
