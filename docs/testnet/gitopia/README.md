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
peers="c03e9f152bb1becc54d4424d02249135d39be09f@81.0.218.106:41656,3989c44e8af3427b22a71a94185e85df99d450b4@149.102.158.188:41656,63381c5528ed8ca93f9ba31008a9630d21b29a97@142.132.152.46:46656,f7de718f3d1b19f30f015f390af2910ef26564eb@121.4.78.114:26656,407eb21b784f1dc4e9902cb812b65eec760c6a19@185.193.66.67:656,ebeba690d8084592a983da1e6429598cc9b9d04c@213.202.212.77:26656,31099d763305ead833b84c28b142ecbfd3628a64@85.190.246.250:41656,afbed8b52881b2f783df0cb07865a4da2fbbdf5e@167.235.243.27:26656,4e4f87cfa1993f4f3f7645c41f469987cafdf960@85.10.202.135:12656,fb0a1c5dbc329b1b0ae3dac6776df4eb5f2072f6@79.137.248.142:26656,1fee6e7fd077911abab93739f6bf13c62dedbf20@178.62.204.49:26656,995177c4b8c2b498de50483a614f9e30bf02e843@65.109.130.180:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,09538ba6159f454a17d76501c59e23bad6fc9d3d@85.190.246.67:26656,02c20307295465ab2592fd81176e66be90d4bbe2@5.189.159.111:26656,2e714e8854361967515a8b859f8f4b0d9b8d11e8@194.163.190.86:26656,f1a47d469460fb0a70b12d7739afbc0bf78eadda@78.47.195.69:656,b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,016b0e565abd496b9473b87ac41339251005d12e@194.163.167.163:41656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,374da78901e59810277fc35482bce6e30953f488@80.79.6.155:41656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,4b74a2394e9c251ca24c68e666288a5fdae78010@185.245.183.246:26656,d15e22d7be8ba1b97ff429cf87fea2af41450b37@149.102.134.212:41656,dea00215e54c4098a4f194a7ecd43e24ea99336f@88.99.95.81:26656,5c2c2b27e1824097d4f5dc7a581a8d615923e76f@185.252.235.110:41656,edae8278cef6113e38af80504fb83cbf5eb0f023@165.232.129.242:26656,6ce7f9ea8e3019c50057f4eb2a0ed55e8eedf874@194.50.0.44:26656,ff4fab3a07cdf3601b90ececd2de9a85b3a1a42e@82.208.21.152:26656,e1ab0573d55ff92fad55d2929e353904f1bbe36f@135.181.16.252:31656,5171aad5f862d474b36fc8049be3339068c96cc9@165.232.151.144:26656,ae5d5b47ea732ff509114f405967f61eb3d86ac6@75.119.146.171:656,0eb70bf5e2403694109f9bba184570074c2dfdd5@38.242.235.255:26656,f7fcda07044dc64cec2f6dca9da0c37a254bbae8@138.201.127.91:26676"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
